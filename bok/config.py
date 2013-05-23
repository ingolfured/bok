import sys
import os
import functools

DIR_NAME = os.path.dirname(__file__)
PATH = functools.partial(os.path.join, DIR_NAME)

sys.path.append(PATH(".."))
