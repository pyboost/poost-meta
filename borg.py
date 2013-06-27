#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Pengkui Luo <pengkui.luo@gmail.com>
# Created 06/27/2013, updated 06/27/2013
#
""" Borg design patterns. (TODO)

    Reference:
    http://code.activestate.com/recipes/66531/
    http://code.activestate.com/recipes/577870/

"""
__all__ = [
    'Borg',
]
print('Executing %s' %  __file__)

import os, sys, time



if __name__ == '__main__':
    t0 = time.time()
    print('Done. Time elapsed: %.2f.' % (time.time() - t0))
