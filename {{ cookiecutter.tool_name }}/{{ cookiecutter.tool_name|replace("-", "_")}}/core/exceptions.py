class {{ cookiecutter.tool_name | capitalize | replace("-", "")}}Error(Exception):
    pass


class {{ cookiecutter.tool_name | capitalize | replace("-", "")}}ValueError(ValueError):
    pass


class {{ cookiecutter.tool_name | capitalize | replace("-", "")}}TypeError(TypeError):
    pass


__all__ = ("{{ cookiecutter.tool_name | capitalize| replace("-", "")}}Error", "{{ cookiecutter.tool_name | capitalize | replace("-", "")}}ValueError", "{{ cookiecutter.tool_name | capitalize | replace("-", "")}}TypeError")
