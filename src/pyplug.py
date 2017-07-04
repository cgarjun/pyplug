import sys
import os
import yaml

class PluginManager(object):
	def __init__(self, config=None):
		self._plugin_config = yaml.load(file(config))
		self.setup()

	def setup(self):
		try:
			sys.path.append(os.path.abspath(self.plugin_config['plugin_path']))
		except KeyError:
			pass

	def import_plugins(self, plugin_name):
		m = __import__(plugin_name)
		return m

	def run_plugin(self, plugin_name):
		args = {}
		plug = self.import_plugins(plugin_name)
		try:
			args = self.plugin_list[plugin_name]['args']
		except KeyError:
			pass
		if self.plugin_list[plugin_name]['enable']:
			plug.main(**args)

	def run_all_plugins(self):
		for plug in self.plugin_list:
			self.run_plugin(plug)

	@property
	def plugin_config(self):
	    return self._plugin_config

	@property
	def plugin_list(self):
	    return self._plugin_config['plugin_list']
