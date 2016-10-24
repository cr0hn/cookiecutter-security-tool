"""
This file contains utils and reusable functions
"""

from collections import namedtuple


def dict_to_obj(data):
    """
    Transform an input dict into a object.
    
    >>> data = dict(hello="world", bye="see you")
    >>> obj = dict_to_obj(data)
    >>> obj.hello
    'world'
    
    :param data: input dictionary data
    :type data: dict
    """
    if not isinstance(data, dict):
        raise TypeError("Expected dict, got '%s' instead" % type(data))
    
    class _tmp(object):
        pass
    
    obj = namedtuple("OBJ", list(data.keys()))
    
    o = obj(**data)
    
    return o

__all__ = ("dict_to_obj", )
