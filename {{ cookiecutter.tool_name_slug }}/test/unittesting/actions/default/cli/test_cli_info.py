import click

from click.testing import CliRunner

from {{ cookiecutter.tool_name_slug }}.actions.default.cli import info

import {{ cookiecutter.tool_name_slug }}.actions.default.console


def _launch_{{ cookiecutter.tool_name_slug }}_in_console(blah, **kwargs):
    click.echo("ok")
    

def test_cli_info_runs_show_help():
    runner = CliRunner()
    result = runner.invoke(info)
    
    assert 'Usage: info [OPTIONS] ' in result.output


def test_cli_info_runs_ok():
    # Patch the launch of: launch_{{ cookiecutter.tool_name_slug }}_info_in_console
    {{cookiecutter.tool_name_slug}}.actions.default.cli.launch_{{ cookiecutter.tool_name_slug }}_in_console = _launch_{{ cookiecutter.tool_name_slug }}_in_console
    
    runner = CliRunner()
    result = runner.invoke(info, ["aaaa"])
    
    assert 'ok' in result.output
