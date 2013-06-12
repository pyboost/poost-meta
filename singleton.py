#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
http://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
http://code.activestate.com/recipes/102187-singleton-as-a-metaclass/
http://stackoverflow.com/questions/674304/pythons-use-of-new-and-init
http://docs.python.org/reference/datamodel.html#basic-customization

"""

__all__ = [
    'Singleton',
    'SingletonInit',
]

class Singleton (type):
    """ Singleton metaclass.
        If an instance of the class exists, just return that instance.
    """
    _instances = {}
    def __call__ (cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonInit (type):
    """ Singleton metaclass.
        If an instance of the class exists, *run the __init__()* for this
        instance, and then return the instance.
    """
    _instances = {}
    def __call__ (cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
        else:  # run __init__ every time the class is called
            cls._instances[cls].__init__(*args, **kwargs)
        return cls._instances[cls]
