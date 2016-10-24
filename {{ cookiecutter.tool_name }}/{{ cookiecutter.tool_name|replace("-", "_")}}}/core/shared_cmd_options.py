import click

# --------------------------------------------------------------------------
# Common options for command line interface
# --------------------------------------------------------------------------
global_options_list = (
    # General
    click.option('-v', 'verbosity', count=True, type=int, default=1, help='Verbose output'),
    click.option('--quiet', '-q', 'verbosity', flag_value=0, help='Minimal output')
)


class global_options(object):
    def __init__(self, invoke_without_command=False):
        self.invoke_without_command = invoke_without_command
    
    def __call__(self, f):
        def wrapped_f(*args):
            fn = f
            for option in reversed(global_options_list):
                fn = option(f)
            
            fn = click.group(context_settings={'help_option_names': ['-h', '--help']},
                             invoke_without_command=self.invoke_without_command)(fn)
            
            return fn
        
        return wrapped_f()


#
# HERE MORE EXAMPLES OF CMD OPTIONS
#
# --------------------------------------------------------------------------
# Options for "auto" command
# --------------------------------------------------------------------------
#
# auto_options_list = (
#     click.option('-T', '--timeout', 'timeout', type=int, default=60,
#                  help="max time to wait until actions are available"),
# )
#
#
# class auto_options(object):
#     def __call__(self, f):
#         def wrapped_f(*args):
#             fn = f
#             for option in reversed(auto_options_list):
#                 fn = option(f)
#
#             return fn
#
#         return wrapped_f()


__all__ = ("global_options",)  # "auto_options")
