#!/usr/bin/python


'''
Main import file used when 'import meraki_cli'
'''


from . import __main__
from .__main__ import *  # Make all the functions and classes available
from . import __version__


name = "meraki_cli"
__version__ = __version__.version
