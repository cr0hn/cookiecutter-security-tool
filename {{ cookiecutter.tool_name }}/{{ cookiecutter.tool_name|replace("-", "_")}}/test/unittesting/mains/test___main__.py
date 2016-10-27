def main():
    import os
    import sys
    
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(1, parent_dir)
    import {{ cookiecutter.tool_name | replace("-", "_") }}
    
    __package__ = str("{{ cookiecutter.tool_name | replace("-", "_") }}")
    
    # Run the cmd
    from {{ cookiecutter.tool_name | replace("-", "_") }}.actions.cli import cli
    
    cli()


if __name__ == "__main__":
    main()  # pragma no cover
