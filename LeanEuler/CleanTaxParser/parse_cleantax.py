from .CleanTaxLexer import CleanTaxLexer
from .CleanTaxParser import CleanTaxParser
from .CleanTaxListener import CleanTaxListener

from antlr4 import *
import pandas as pd

from anytree import Node

# EDGE_TYPES
PARENT = "parent"
IS_INCLUDED_IN = "<"
INCLUDES = ">"
EQUALS = "="
DISJOINT = "!"
OVERLAPS = "o"


def gen_node_name(node: str, tax_name: str):
    return "\"{}_{}\"".format(tax_name, node)


# Convert a given relation to one of the aboe edge types
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
        self.data = {
            'taxonomies': {},
            'current_taxonomy': None,
            'current_articulation': None,
            'articulation_list': [],
            'relation_data': None,
        }

    def enterTax_desc(self, ctx):

        tax_name = []
        i = 0
        while ctx.TEXT(i) is not None:
            tax_name.append(ctx.TEXT(i).getText())
            i += 1

        self.data['current_taxonomy'] = tax_name[0]
        self.data['taxonomies'][tax_name[0]] = {tax_name[0]: Node(tax_name[0])}

    def enterTax_sub_desc(self, ctx):

        i = 0
        parent = None
        children = []
        while ctx.TEXT(i) is not None:
            node_name = ctx.TEXT(i).getText().strip()
            if i == 0:
                parent = node_name
            else:
                children.append(node_name)
            i += 1

        if (parent != None) and (parent not in self.data['taxonomies'][self.data['current_taxonomy']]):
            self.data['taxonomies'][self.data['current_taxonomy']][parent] = Node(
                gen_node_name(parent, self.data['current_taxonomy']),
                parent=self.data['taxonomies'][self.data['current_taxonomy']][self.data['current_taxonomy']])
            # self.data['articulation_list'].append(("{}".format(self.data['current_taxonomy']),
            # PARENT, "{}.{}".format(self.data['current_taxonomy'], parent)))

        for child in children:
            self.data['taxonomies'][self.data['current_taxonomy']][child] = Node(
                gen_node_name(child, self.data['current_taxonomy']),
                parent=self.data['taxonomies'][self.data['current_taxonomy']][parent])
            self.data['articulation_list'].append((gen_node_name(parent, self.data['current_taxonomy']), PARENT,
                                                   gen_node_name(child, self.data['current_taxonomy'])))

    def exitTax_desc(self, ctx):
        self.data['current_taxonomy'] = None

    def enterRcc5_rel(self, ctx):
        if ctx.RCC_BASIC_5 is not None:
            self.data['current_relation'] = [rcc_basic_5_to_edge_type(ctx.RCC_BASIC_5().getText().strip())]

    def enterRcc32_rel(self, ctx):

        i = 0
        rls = []
        while ctx.RCC_BASIC_5(i) is not None:
            rls.append(ctx.RCC_BASIC_5(i).getText().strip())
            i += 1

        rls = list(map(rcc_basic_5_to_edge_type, rls))
        self.data['current_relation'] = rls

    def exitArticulation(self, ctx):

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
        self.data['articulation_list'].append((gen_node_name(node1, tax1), rl_type_str, gen_node_name(node2, tax2)))
        self.data['current_relation'] = None

    def exitCt_input(self, ctx):
        self.data['relation_data'] = pd.DataFrame(self.data['articulation_list'],
                                                  columns=['Node1', 'Relation', 'Node2'])


def parse_cleantax(fname):
    filestream = FileStream(fname)
    lexer = CleanTaxLexer(filestream)
    stream = CommonTokenStream(lexer)
    parser = CleanTaxParser(stream)
    tree = parser.ct_input()
    # print (Trees.toStringTree(tree, None, parser))
    clean_tax_listener = AntlrCleanTaxListener()
    walker = ParseTreeWalker()
    walker.walk(clean_tax_listener, tree)

    return clean_tax_listener.data['relation_data'], clean_tax_listener.data['taxonomies']



