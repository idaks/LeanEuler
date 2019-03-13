import errno
import inspect
import os


# Folder and File name conventions

PICKLE_FOLDER = ".le_temp_pickle_data"
CLEANTAX_INPUT_FOLDER = 'LE_Preprocessed_CleanTax_Input'
TAX_DESC_PANDAS_FILE = 'taxDesc'
ANYTREE_FILE = 'anytree'
CLINGO_FILES_FOLDER = 'LE_Clingo_Files'

# to help debug


def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno


# helper funcs


def isfloat(value):
    """
    returns true if a value can be typecasted as a float, else false
    """
    try:
        float(value)
        return True
    except ValueError:
        return False


def mkdir_p(path):
    """
    make a directory if it doesn't already exist
    """
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise
