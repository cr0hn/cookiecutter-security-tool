
from {{ cookiecutter.tool_name  | replace("-", "_") }} import SharedConfig, String


class {{ cookiecutter.tool_name | capitalize  | replace("-", "") }}Model(SharedConfig):
    target = String()
    
__all__ = ("{{ cookiecutter.tool_name | capitalize | replace("-", "_") }}Model", )


