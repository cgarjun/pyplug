import os
import imp
import yaml
import plugexception

class PyPlug(object):
    def __init__(self, **entry):
        self.__dict__.update(entry)

    def execute(self):
        loadFile = os.path.join(self.pluginpath, "{0}.py".format(self.name))
        module = imp.load_source(self.name, loadFile)
        if self.enable:
            try:
                module.main(**self.args)
            except AttributeError:
                module.main()
        else:
            print('Plugin is disabled')

class PluginManager(object):
    """
    Simple plugin manager works based on configuration files

    Example:
            from pyplug import PluginManager
            pm = PluginManager('config.yaml')
            pm.runPlugin('plugin_a')
            or
            pm.runPlugins()

    Attributes:
            config (path): Configuration file that defines the search path and
            plugin information in yaml format
    """
    def __init__(self, config):
        self._config = config
        try:
            self._plug = yaml.load(file(self.config))
        except yaml.scanner.ScannerError:
            msg ='Unable to register plugin configuration, check yaml syntax'
            raise plugexception.PluginRegisterError(msg)
        

    def listPlugins(self):
        '''
        Lists all the plugins registered from the config file

        Returns:
            list: List of plugins names as strin
        '''
        try:
            all_plugins = self._plug['plugins']
        except KeyError:
            raise plugexception.PluginError('No plugins registered')

        try:
            return all_plugins.keys()
        except AttributeError:
            raise plugexception.PluginError('No plugins registered')


    def getPlugin(self, pluginName):
        '''
        Gets the config information for a specific plugin

        Returns:
            dict: plugin parameters in key value pair

        '''
        try:
            plugData = self._plug['plugins'][pluginName]
            plugData['name'] = pluginName
            plugData['pluginpath'] = self.pluginpath
        except KeyError:
            plugexception.PluginNotFoundError('Unable to find plugin')
        return PyPlug(**plugData)

    def runPlugin(self, pluginName):
        '''
        Executes all the specific plugin as per specified argument

        Attributes:
            pluginName: Name of a specific plugin mentioned in the 
            configuration file
        '''
        plugin = self.getPlugin(pluginName)
        plugin.execute()
        return True

    def runPlugins(self):
        '''
        Executes all the plugins defined in the configuration file
        '''
        for plug in self.listPlugins():
            self.runPlugin(plug)

        return True

    @property
    def config(self):
        return self._config

    @property
    def pluginpath(self):
        return self._plug['pluginpath']
