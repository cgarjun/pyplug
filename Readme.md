# pyplug
This is simple plugin system based out of python, you can basically pass a config file with all necessary requirements and get the plugins to be executed

## Requirements
```python
Python 2.7+
pip install PyYaml
```

## example_config

Simple example of how config should be formatted. This is basically yaml format and easy human readable
```
pluginpath: D:\development\pyplug\example_plugins
plugins:
  plugin_name_a:
    enable: true
    args:
      arg_a: blah
      arg_b: hello

  plugin_name_b:
    enable: false

  plugin_name_c:
    enable: true
    args:
      arg_a: blah
      arg_b: hello
```

## example_plugins

This is also extremly simple make any python file with a main function

## Usage
```python
from pyplug import PluginManager

pm = PluginManager('../example_config/plugins.yaml')
pm.runPlugins()
or
pm.runPlugin('plugin_b')
```
List all availabel plugins from the config

```pm.listPlugins()
['plugin_a', 'plugin_b']
```
Get the plugin object separate and execute it independent
```pl = pm.getPlugin('plugin_name_a')
print pl.enable
print pl.args


pl.execute()
```
