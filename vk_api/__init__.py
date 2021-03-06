'''
@author: Kirill Python
@contact: http://vk.com/python273
@license Apache License, Version 2.0, see LICENSE file

Copyright (C) 2013
'''

__author__ = "Kirill Python"
__version__ = "4.6"
__email__ = "mikeking568@gmail.com"
__contact__ = "https://vk.com/python273"

import sys

if sys.version_info[0] == 2:
    from vk_api import *
    from vk_upload import *
else:
    from .vk_api import *
    from .vk_upload import *
