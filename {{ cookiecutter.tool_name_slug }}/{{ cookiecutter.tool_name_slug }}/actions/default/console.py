import logging

from .model import *
from ..helpers import *

log = logging.getLogger('{{ cookiecutter.tool_name_slug }}')


def launch_{{ cookiecutter.tool_name_slug }}_in_console(shared_config, **kwargs):
    """Launch in console mode"""
    
    # Load config
    config = {{ cookiecutter.tool_name_camel_case }}DefaultModel(**shared_config, **kwargs)
    
    # Check if config is valid
    if not config.is_valid:
        for prop, msg in config.validation_errors:
            log.critical("[!] '%s' property %s" % (prop, msg))
        return
    
    log.setLevel(config.verbosity)
    
    try:
        log.console("Info runs!")
    
    except KeyboardInterrupt:
        log.console("[*] CTRL+C caught. Exiting...")
    except Exception as e:
        log.critical("[!] Unhandled exception: %s" % str(e))
        
        log.exception("[!] Unhandled exception: %s" % e, stack_info=True)
    finally:
        log.debug("[*] Shutdown...")
        

__all__ = ("launch_{{ cookiecutter.tool_name }}_in_console",)
