import pytest

from {{ cookiecutter.tool_name_slug }}.actions.default.api import run_default_{{ cookiecutter.tool_name_slug }}


def test_run_default_{{ cookiecutter.tool_name_slug }}_runs_ok():

    #
    # FILL THIS WITH A TEST
    #
    # assert run_default_{{ cookiecutter.tool_name_slug }}() is None
    pass


def test_run_default_{{ cookiecutter.tool_name_slug }}_empty_input():

    with pytest.raises(AssertionError):
        run_default_{{ cookiecutter.tool_name_slug }}(None)
