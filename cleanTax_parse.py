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


#class AntlrCleanTaxListener(CleanTaxListener):






input = FileStream('cleantax_sample.txt')
lexer = CleanTaxLexer(input)
stream = CommonTokenStream(lexer)
parser = CleanTaxParser(stream)
tree = parser.ct_input()
print Trees.toStringTree(tree, None, parser)