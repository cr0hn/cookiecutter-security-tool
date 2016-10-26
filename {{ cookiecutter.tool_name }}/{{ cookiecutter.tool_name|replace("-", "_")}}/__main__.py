if __name__ == "__main__":
    import os
    import sys
    
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(1, parent_dir)
    import {{ cookiecutter.tool_name}}
    
    __package__ = str("{{ cookiecutter.tool_name}}")
    
    # Run the cmd
    from .actions.cli import cli
    
    cli()
