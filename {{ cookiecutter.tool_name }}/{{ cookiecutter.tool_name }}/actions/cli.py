#!/usr/bin/env python3

import click
import logging

from {{ cookiecutter.tool_name }} import global_options

from .console import launch_{{ cookiecutter.tool_name }}_in_console


log = logging.getLogger('{{ cookiecutter.tool_name }}')


@global_options()
@click.pass_context
def cli(ctx, **kwargs):
    ctx.obj = kwargs


@cli.command(help="Launch {{ cookiecutter.tool_name }}")
@click.pass_context
@click.argument('target', required=True)
def info(ctx, **kwargs):
    """Launch a Golismero Scan"""
    
    launch_{{cookiecutter.tool_name}}_in_console(ctx.obj, **kwargs)


if __name__ == "__main__" and __package__ is None:
    cli()
