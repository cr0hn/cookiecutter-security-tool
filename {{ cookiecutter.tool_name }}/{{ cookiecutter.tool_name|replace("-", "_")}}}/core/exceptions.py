class {{ cookiecutter.tool_name | capitalize }}Error(Exception):
    pass


class {{ cookiecutter.tool_name | capitalize }}ValueError(ValueError):
    pass


class {{ cookiecutter.tool_name | capitalize }}TypeError(TypeError):
    pass


__all__ = ("{{ cookiecutter.tool_name | capitalize}}Error", "{{ cookiecutter.tool_name | capitalize}}ValueError", "{{ cookiecutter.tool_name | capitalize}}TypeError")
