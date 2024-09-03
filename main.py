from plugin_core import PluginRegistryMeta
import os, importlib


def search_for_plugins():
    print("Pesquisando por plugins")
    plugins_path = os.path.join(os.path.dirname(__file__), "plugins")
    # se a pasta plugins existir
    if os.path.exists(plugins_path):
        for plugin_dir in os.listdir(plugins_path):
            # no nosso caso, convencionamos que os plugins ficariam dentro de pastas
            if not os.path.isdir(os.path.join(plugins_path, plugin_dir)):
                continue
            # se essa pasta conter o arquivo plugin.py (ou plugin.pyc para versões compiladas)
            for plugin_file in os.listdir(os.path.join(plugins_path, plugin_dir)):
                if plugin_file == "plugin.py" or plugin_file == "plugin.pyc":
                    # caso sim, realizaremos a importação do módulo via importlib
                    importlib.import_module(f"plugins.{plugin_dir}.plugin")
                    break
    return PluginRegistryMeta.registered_plugins


if __name__ == "__main__":
    plugins = search_for_plugins()
    if len(plugins) == 0:
        print("Nenhum plugin carregado")
    else:
        for plugin in plugins:
            print(f"Plugin {plugin.get_plugin_name()} disponível")
