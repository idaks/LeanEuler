import errno
import inspect
import sys
from sys import argv
import string
import os


###################################################################

#to help debug
def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno

###################################################################

###################################################################

#helper funcs

def isfloat(value):
  """returns true if a value can be typecasted as a float, else false"""
  try:
    float(value)
    return True
  except ValueError:
    return False

def mkdir_p(path):
    """make a directory if it doesn't already exist"""
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

###################################################################

