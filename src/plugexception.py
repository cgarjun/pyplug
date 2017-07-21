class PluginRegisterError(Exception):
	def __init__(self, message):
		super(PluginRegisterError, self).__init__(message)

class PluginEnableError(Exception):
	def __init__(self, message):
		super(PluginEnableError, self).__init__(message)

class PluginNotFoundError(Exception):
	def __init__(self, message):
		super(PluginNotFoundError, self).__init__(message)

class PluginError(Exception):
	def __init__(self, message):
		super(PluginError, self).__init__(message)
