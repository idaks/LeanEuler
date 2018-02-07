#!/usr/bin/env python3

import sys
import time
from sys import argv
from antlr4 import *
from CleanTaxLexer import CleanTaxLexer
from CleanTaxParser import CleanTaxParser
from CleanTaxListener import CleanTaxListener
import pandas as pd
import numpy as np
from antlr4.tree.Trees import Trees
import os
import string
import argparse
import pickle
from anytree import Node, RenderTree
from graphviz import Digraph
from helper import lineno, isfloat, mkdir_p


#EDGE_TYPES
PARENT = "parent"
IS_INCLUDED_IN = "<"
INCLUDES = ">"
EQUALS = "="
DISJOINT = "!"
OVERLAPS = "o"

def rcc_basic_5_to_edge_type(rl):

	if rl in ['><', 'o', 'overlaps']:
		return OVERLAPS
	elif rl in ['<', 'is_included_in']:
		return IS_INCLUDED_IN
	elif rl in ['>', 'includes']:
		return INCLUDES
	elif rl in ['==', '=', 'equals']:
		return EQUALS
	elif rl in ['!', 'disjoint']:
		return DISJOINT

	return PARENT



class AntlrCleanTaxListener(CleanTaxListener):

	def __init__(self):
		self.data = {'taxonomies' : {},
					 'graphviz_tree' : Digraph(comment='Taxonomies'),
					 'current_taxonomy': None,
					 'current_articulation': None,
					 'articulation_list' : []
					}

	def enterTax_desc(self, ctx):

		tax_name = []
		i = 0
		while ctx.TEXT(i) is not None:
			tax_name.append(ctx.TEXT(i).getText())
			i += 1

		self.data['current_taxonomy'] = tax_name[0]
		print (tax_name)

		self.data['taxonomies'][tax_name[0]] = {tax_name[0]: Node(tax_name[0])}
		self.data['graphviz_tree'].node(tax_name[0])


	def enterTax_sub_desc(self, ctx):

		# print ("HERE")
		# print (self.data['current_taxonomy'])
		# print (self.data['taxonomies'])

		i = 0
		parent = None
		children = []
		while ctx.TEXT(i) is not None:

			node_name = ctx.TEXT(i).getText().strip()
			#print (node_name)
			if i == 0:
				parent = node_name
			else:
				children.append(node_name)

			i+=1


		#print ("parent:", parent)
		#print ("children:", children)

		if (parent != None) and (parent not in self.data['taxonomies'][self.data['current_taxonomy']]):

			self.data['taxonomies'][self.data['current_taxonomy']][parent] = Node(parent, parent = self.data['taxonomies'][self.data['current_taxonomy']][self.data['current_taxonomy']])
			self.data['graphviz_tree'].node("{}.{}".format(self.data['current_taxonomy'],parent))
			self.data['graphviz_tree'].edge(tail_name = self.data['current_taxonomy'], head_name = "{}.{}".format(self.data['current_taxonomy'],parent), label = PARENT, type = PARENT)

		for child in children:

			self.data['taxonomies'][self.data['current_taxonomy']][child] = Node(child, parent = self.data['taxonomies'][self.data['current_taxonomy']][parent])
			self.data['graphviz_tree'].node("{}.{}".format(self.data['current_taxonomy'],child))
			self.data['graphviz_tree'].edge(tail_name = "{}.{}".format(self.data['current_taxonomy'],parent), head_name = "{}.{}".format(self.data['current_taxonomy'],child), label = PARENT, type = PARENT)



	def exitTax_desc(self, ctx):

		print(RenderTree(self.data['taxonomies'][self.data['current_taxonomy']][self.data['current_taxonomy']]))
		
		self.data['current_taxonomy'] = None


	def enterRcc5_rel(self, ctx):

		if ctx.RCC_BASIC_5 is not None:

			self.data['current_relation'] = [rcc_basic_5_to_edge_type(ctx.RCC_BASIC_5().getText().strip())]

	def enterRcc32_rel(self, ctx):

		i = 0
		rls = []
		while ctx.RCC_BASIC_5(i) is not None:
			rls.append(ctx.RCC_BASIC_5(i).getText().strip())
			i+=1

		rls = list(map(rcc_basic_5_to_edge_type, rls))
		self.data['current_relation'] = rls


	def exitArticulation(self, ctx):

		node1 = None
		node2 = None

		if ctx.TEXT(0) is None or ctx.TEXT(1) is None:
			return

		node1 = ctx.TEXT(0).getText().strip()
		node2 = ctx.TEXT(1).getText().strip()

		node1 = node1.split('.')
		tax1 = node1[0]
		node1 = node1[1]

		node2 = node2.split('.')
		tax2 = node2[0]
		node2 = node2[1]

		self.data['current_relation'].sort()
		rl_type_str = ','.join(map(str, self.data['current_relation']))
		self.data['graphviz_tree'].edge(tail_name = "{}.{}".format(tax1, node1), head_name = "{}.{}".format(tax2, node2), label = rl_type_str, type = rl_type_str)
		self.data['articulation_list'].append(("{}.{}".format(tax1, node1), rl_type_str, "{}.{}".format(tax2, node2)))
		self.data['current_relation'] = None

	def exitCt_input(self, ctx):
		#print (self.data['taxonomies'])
		#print (self.data['current_taxonomy'])
		self.data['graphviz_tree'].render(view=True)
		print (self.data['graphviz_tree'].source)
		df = pd.DataFrame(self.data['articulation_list'], columns = ['Node1', 'Relation', 'Node2'])
		print (df)
		self.data = {}



script, file = argv
file = FileStream(file)
lexer = CleanTaxLexer(file)
stream = CommonTokenStream(lexer)
parser = CleanTaxParser(stream)
tree = parser.ct_input()
#print (Trees.toStringTree(tree, None, parser))
lean_euler = AntlrCleanTaxListener()
walker = ParseTreeWalker()
walker.walk(lean_euler, tree)
