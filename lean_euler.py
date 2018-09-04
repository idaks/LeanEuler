#!/usr/bin/env python3
from preprocess_clean_tax import preprocess_clean_tax
from generate_ASP import generate_asp
import cleanTax_parse
import os
from antlr4 import FileStream


class LeanEuler:

    @staticmethod
    def parse_cleantax(clean_tax_lines):

        preprocessed_clean_tax = preprocess_clean_tax(clean_tax_lines)
        fname = 'jkbdbcjbdhscbjhbsnkjbjshudhcbskncbhsdbcsbdhbcsbcbshjbdcsjbiueryanballps.txt'
        # clean_tax_stream = StringIO()
        # clean_tax_stream.write('\n'.join(preprocessed_clean_tax))
        with open(fname, 'w') as f:
            f.write('\n'.join(preprocessed_clean_tax))
        clean_tax_stream = FileStream(fname)
        os.remove(fname)
        return cleanTax_parse.parse_cleantax(clean_tax_stream)

    @staticmethod
    def gen_asp_rules(relation_data, anytree_data, encoding='mnpw', reasoner='clingo'):
        return generate_asp(relation_data, anytree_data, encoding)

    @staticmethod
    def gen_asp_rules_from_cleantax(clean_tax_lines, encoding='mnpw', reasoner='clingo'):
        relation_data, anytree_data = LeanEuler.parse_cleantax(clean_tax_lines)
        return LeanEuler.gen_asp_rules(relation_data, anytree_data, encoding, reasoner)
