#!/usr/bin/env python3
import argparse
import pandas as pd
import pickle
import numpy as np
import os
from helper import lineno, isfloat, mkdir_p, get_rcc_rules

PICKLE_FOLDER = "Temp_Pickle_Data"
TAX_DESC_PANDAS_FILE = 'taxDesc'
CLINGO_FILES_FOLDER = "Clingo_Input_Files"
NODE1_COL = 'Node1'
NODE2_COL = 'Node2'
REL_COL = 'Relation'

#EDGE_TYPES
PARENT = "parent"
IS_INCLUDED_IN = "<"
INCLUDES = ">"
EQUALS = "="
DISJOINT = "!"
OVERLAPS = "o"

def gen_node_name(node_name, taxonomy_dict):

	tax_name = node_name.split('.')[0]
	if tax_name not in taxonomy_dict:
		taxonomy_dict[tax_name] = chr(ord('a') + len(taxonomy_dict))

	return "{}{}".format(taxonomy_dict[tax_name], node_name.replace(".", "_"))

def get_rule(node1, rl, node2):

	rl_asp_dict = {PARENT : 'bl',
				   IS_INCLUDED_IN: 'pp',
				   INCLUDES: 'pi',
				   EQUALS: 'eq',
				   DISJOINT: 'dr',
				   OVERLAPS: 'po'}

	if rl in rl_asp_dict:
		return "{}({},{})".format(rl_asp_dict[rl], node1, node2)
	#print("rl {} not found".format(rl))
	return ""


def get_asp_rule(node1, rls, node2):

	#print ("Get ASP rule called with {}, {}, {}".format(node1, rls, node2))
	if len(rls) > 1:
		rules = [get_rule(node1, rl, node2) for rl in rls]
		return "1 {{ {0} }}.".format(" ; ".join(rules))
	elif len(rls) == 1:
		return "{}.".format(get_rule(node1, rls[0], node2))
	return ""

def __main__():

	parser = argparse.ArgumentParser()
	parser.add_argument("project_name", type = str, help = "provide session/project name used while preprocessing and/or parsing")
	args = parser.parse_args()

	project_name = args.project_name
	relations_file = PICKLE_FOLDER + '/' + project_name + '/' + TAX_DESC_PANDAS_FILE + '.pkl'

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

	clingo_file = open(CLINGO_FILES_FOLDER + '/' + str(project_name) + '.lp4', 'w')

	rules_to_write = get_rcc_rules()
	rules_to_write.append("%TAXONOMY DESC RULES\n")
	taxonomy_dict = {}

	for index, row in df.iterrows():

		node1 = row[NODE1_COL]
		relations = row[REL_COL]
		node2 = row[NODE2_COL]

		node1 = gen_node_name(node1, taxonomy_dict)
		node2 = gen_node_name(node2, taxonomy_dict)

		asp_rule = get_asp_rule(node1, relations.split(","), node2)
		#print (asp_rule)
		rules_to_write.append(asp_rule)

	clingo_file.writelines("\n".join(rules_to_write))



if __name__ == '__main__':
	__main__()