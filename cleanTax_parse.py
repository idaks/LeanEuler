#!/usr/bin/env python3

import sys
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


class AntlrCleanTaxListener(CleanTaxListener):

	def __init__(self):
		self.data = {'taxonomies' : {}, 
					 'articulations': [], 
					 'current_taxonomy': None,
					 'current_articulation': None}

	def exitCt_input(self, ctx):
		#print (self.data['taxonomies'])
		#print (self.data['current_taxonomy'])
		self.data = {}

	def enterTax_desc(self, ctx):

		tax_name = []
		i = 0
		while ctx.TEXT(i) is not None:
			tax_name.append(ctx.TEXT(i).getText())
			i += 1

		self.data['current_taxonomy'] = tax_name[0]
		print (tax_name)

		self.data['taxonomies'][tax_name[0]] = {tax_name[0]: Node(tax_name[0])}


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

		for child in children:

			self.data['taxonomies'][self.data['current_taxonomy']][child] = Node(child, parent = self.data['taxonomies'][self.data['current_taxonomy']][parent])


	def exitTax_desc(self, ctx):

		print(RenderTree(self.data['taxonomies'][self.data['current_taxonomy']][self.data['current_taxonomy']]))

		self.data['current_taxonomy'] = None








        

		





input = FileStream('cleantax_sample.txt')
lexer = CleanTaxLexer(input)
stream = CommonTokenStream(lexer)
parser = CleanTaxParser(stream)
tree = parser.ct_input()
#print (Trees.toStringTree(tree, None, parser))
lean_euler = AntlrCleanTaxListener()
walker = ParseTreeWalker()
walker.walk(lean_euler, tree)
