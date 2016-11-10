class {{ cookiecutter.tool_name_camel_case }}Error(Exception):
    pass


class {{ cookiecutter.tool_name_camel_case }}ValueError(ValueError):
    pass


class {{ cookiecutter.tool_name_camel_case }}TypeError(TypeError):
    pass


__all__ = ("{{ cookiecutter.tool_name_camel_case }}Error", "{{ cookiecutter.tool_name_camel_case }}ValueError", "{{ cookiecutter.tool_name_camel_case }}TypeError")
