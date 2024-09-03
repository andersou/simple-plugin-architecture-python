from plugin_core import PluginBase


class Project1Plugin(PluginBase):

    @classmethod
    def get_plugin_name(cls) -> str:
        return "Project1Plugin"
