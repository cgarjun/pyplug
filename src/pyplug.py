import os
import yaml

class PluginManager(object):
	def __init__(self, config=None):
		self._plugin_config = yaml.load(file('plugins.yaml', 'r'))

	def import_plugins(self, plugin_name):
		m = __import__(plugin_name)
		return m

	def run_plugin(self, plugin_name, args_dict):
		plug = self.import_plugins(plugin_name)
		plug.main(**args_dict)

	def run_all_plugins(self):
		for i in self.plugin_list:
			self.run_plugin(i, self.plugin_list[i])

	@property
	def plugin_config(self):
	    return self._plugin_config

	@property
	def plugin_list(self):
	    return self._plugin_config['plugin_list']
	
