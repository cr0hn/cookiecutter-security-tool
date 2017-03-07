import click
import logging

from .model import {{ cookiecutter.tool_name_camel_case }}DefaultModel
from .console import launch_{{ cookiecutter.tool_name_slug }}_default_in_console
from ..helpers import check_console_input_config


log = logging.getLogger('{{ cookiecutter.tool_name_slug }}')


@click.command(help="Launch {{ cookiecutter.tool_name }}")
@click.pass_context
@click.argument('target', required=True)
def info(ctx, **kwargs):
    config = {{ cookiecutter.tool_name_camel_case }}DefaultModel(**ctx.obj, **kwargs)

    # Check if valid
    if check_console_input_config(config):
        launch_{{cookiecutter.tool_name_slug}}_default_in_console(config)


__all__ = ("info", )
