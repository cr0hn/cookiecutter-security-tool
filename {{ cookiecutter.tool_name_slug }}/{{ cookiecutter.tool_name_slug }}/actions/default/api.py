from .model import *


def run_default_{{ cookiecutter.tool_name_slug }}(config: {{ cookiecutter.tool_name_camel_case }}DefaultModel):
    assert isinstance(config, {{ cookiecutter.tool_name_camel_case }}DefaultModel)


__all__ = ("run_default_{{ cookiecutter.tool_name_slug }}", )
