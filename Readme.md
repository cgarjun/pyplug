# pyplug
This is simple plugin system based out of python, you can basically pass a config file with all necessary requirements and get the plugins to be executed

## Requirements
```python
Python 2.7
pip install PyYaml
```

## example_config

Simple example of how config should be formatted. This is basically yaml format and easy human readable

## example_plugins

This is also extremly simple make any python file with a main function

## Usage
```python
from pyplug import PluginManager

pm = PluginManager(os.path.abspath('../example_config/plugins.yaml'))
pm.run_all_plugins()
or
pm.run_plugin('plugin_b')
```
