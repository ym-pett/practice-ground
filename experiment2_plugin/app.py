import importlib

PLUGIN_NAME = "plugins.two"

plugin_module = importlib.import_module(PLUGIN_NAME, ".")

print(plugin_module)

plugin = plugin_module.Plugin()

print(plugin.execute(5,3))

