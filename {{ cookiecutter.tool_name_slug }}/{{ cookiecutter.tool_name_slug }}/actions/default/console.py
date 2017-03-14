import logging

from .api import *
from .model import *
from ...core.helpers import *

log = logging.getLogger('{{ cookiecutter.tool_name_slug }}')


def launch_{{ cookiecutter.tool_name_slug }}_default_in_console(config: {{ cookiecutter.tool_name_camel_case }}DefaultModel):
    """Launch in console mode"""

    log.setLevel(config.verbosity)

    with run_in_console(config.debug):
        log.console("Starting analysis...")

        run_default_{{cookiecutter.tool_name_slug}}(config)


__all__ = ("launch_{{ cookiecutter.tool_name }}_in_console",)
