from abc import ABCMeta


class PluginRegistryMeta(ABCMeta):
    registered_plugins = []

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        if name != "PluginBase":
            print(f"Plugin {name} encontrado")
            PluginRegistryMeta.registered_plugins.append(cls)


from abc import abstractmethod


class PluginBase(metaclass=PluginRegistryMeta):

    @classmethod
    @abstractmethod
    def get_plugin_name() -> str:
        pass
