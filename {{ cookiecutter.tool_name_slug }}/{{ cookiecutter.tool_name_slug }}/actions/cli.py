import click
import logging

from {{ cookiecutter.tool_name_slug }} import global_options

from .default.cli import info

log = logging.getLogger('{{ cookiecutter.tool_name_slug }}')


@global_options()
@click.pass_context
def cli(ctx, **kwargs):
    ctx.obj = kwargs

cli.add_command(info)


if __name__ == "__main__" and __package__ is None:  # pragma no cover
    cli()
