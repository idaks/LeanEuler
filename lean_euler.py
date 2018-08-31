#!/usr/bin/env python3
from preprocess_clean_tax import preprocess_clean_tax
from generate_ASP import generate_asp
from cleanTax_parse import parse_cleantax
import os
from antlr4 import FileStream


def gen_asp_from_cleantax(clean_tax_lines, encoding='mnpw', reasoner='clingo'):

    preprocessed_clean_tax = preprocess_clean_tax(clean_tax_lines)
    fname = 'jkbdbcjbdhscbjhbsnkjbjshudhcbskncbhsdbcsbdhbcsbcbshjbdcsjbiueryanballps.txt'
    #clean_tax_stream = StringIO()
    #clean_tax_stream.write('\n'.join(preprocessed_clean_tax))
    with open(fname, 'w') as f:
        f.write('\n'.join(preprocessed_clean_tax))
    clean_tax_stream = FileStream(fname)
    relation_data, anytree_data = parse_cleantax(clean_tax_stream)
    asp_rules = generate_asp(relation_data, anytree_data, encoding)
    os.remove(fname)

    return asp_rules, relation_data, anytree_data
