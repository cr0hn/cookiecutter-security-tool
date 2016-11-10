
from {{ cookiecutter.tool_name_slug }} import SharedConfig, String


class {{ cookiecutter.tool_name_camel_case }}DefaultModel(SharedConfig):
    target = String()
    
__all__ = ("{{ cookiecutter.tool_name_camel_case }}DefaultModel", )


