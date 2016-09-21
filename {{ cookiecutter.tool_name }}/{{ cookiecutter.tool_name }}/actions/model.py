
from {{ cookiecutter.tool_name }} import SharedConfig, String


class {{ cookiecutter.tool_name }}Model(SharedConfig):
    target = String()
    
__all__ = ("{{ cookiecutter.tool_name }}Model", )


