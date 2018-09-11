#!/usr/bin/env python3
import argparse
import pandas as pd
import pickle
import anytree
import numpy as np
import os
from lean_euler_helper_funcs import lineno, isfloat, mkdir_p

PICKLE_FOLDER = "Temp_Pickle_Data"
TAX_DESC_PANDAS_FILE = 'taxDesc'
CLINGO_FILES_FOLDER = "Clingo_Input_Files"
ANYTREE_FILE = 'anytree'


def __main__():

    parser = argparse.ArgumentParser()
    parser.add_argument("project_name", type = str, help = "provide session/project name used while preprocessing and/or parsing")
    parser.add_argument("-encoding", choices=('rcc', 'mnpw'), default='mnpw', help="Select the encoding you want to use. 'rcc' or 'mnpw'")
    args = parser.parse_args()

    project_name = args.project_name
    relations_file = PICKLE_FOLDER + '/' + project_name + '/' + TAX_DESC_PANDAS_FILE + '.pkl'
    anytree_file = PICKLE_FOLDER + '/' + project_name + '/' + ANYTREE_FILE + '.pkl'

    if not os.path.exists(relations_file):
        print ("No file by the name {}.pkl exists in the {} folder. Please recheck the project name.".format(TAX_DESC_PANDAS_FILE, PICKLE_FOLDER+'/'+project_name))
        exit(1)

    df = None
    try:
        with open(relations_file, 'rb') as input_file:
            df = pickle.load(input_file)
    except IOError:
        print ("Could not find the project, check project/session name entered.")
        exit(1)

    anytree_ = None
    try:
        with open(anytree_file, 'rb') as f:
            anytree_ = pickle.load(f)
    except IOError:
        print("Could not find the anytree file. Check the project/session name.")
        exit(1)

    rules_to_write = generate_asp(df, anytree_, args.encoding)

    clingo_file = open(CLINGO_FILES_FOLDER + '/' + str(project_name) + '.lp4', 'w')
    clingo_file.writelines("\n".join(rules_to_write))
    clingo_file.close()


def generate_asp(relations_data, anytree_data, encoding='mnpw'):

    get_rules_func = None
    if encoding == 'rcc':
        from rcc_encoding import get_rules
        get_rules_func = get_rules
    else:
        from mnpw_encoding import get_rules
        get_rules_func = get_rules

    rules_to_write = get_rules_func(relations_data, anytree_data)

    return rules_to_write


if __name__ == '__main__':
    __main__()