#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = [
    'Singleton',
]

class Singleton (type):
    """Singleton metaclass

    http://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
    http://code.activestate.com/recipes/102187-singleton-as-a-metaclass/
    http://stackoverflow.com/questions/674304/pythons-use-of-new-and-init
    http://docs.python.org/reference/datamodel.html#basic-customization
    """
    _instances = {}
    def __call__ (cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
        else:  # run __init__ every time the class is called
            cls._instances[cls].__init__(*args, **kwargs)
        return cls._instances[cls]

