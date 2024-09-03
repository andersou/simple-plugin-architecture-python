from plugin_core import PluginBase


class Project2Plugin(PluginBase):

    @classmethod
    def get_plugin_name(cls) -> str:
        return "Project2Plugin"
