import os

from .CleanTaxParser.parse_cleantax import parse_cleantax
from .Visualizations.euler_input_visualization_nxpd import visualize_euler_input
from .ASPEncodings.rcc_encoding import get_rules as rcc_get_rules
from .ASPEncodings.mnpw_encoding import get_rules as mnpw_get_rules


class LeanEuler:

    @staticmethod
    def preprocess_clean_tax(clean_tax_lines):
        def is_an_empty_line(line):
            return line.strip() == ''

        def is_a_comment(line):
            return line.strip()[0] == '#'

        preprocessed_data = [line for line in clean_tax_lines if
                             (not is_an_empty_line(line)) and (not is_a_comment(line))]
        return preprocessed_data

    @staticmethod
    def parse_cleantax(clean_tax_lines):

        preprocessed_clean_tax = LeanEuler.preprocess_clean_tax(clean_tax_lines)
        fname = 'jkbdbcjbdhscbjhbsnkjbjshudhcbskncbhsdbcsbdhbcsbcbshjbdcsjbiueryanballps.txt'
        # clean_tax_stream = StringIO()
        # clean_tax_stream.write('\n'.join(preprocessed_clean_tax))
        with open(fname, 'w') as f:
            f.write('\n'.join(preprocessed_clean_tax))
        rel_data, taxes = parse_cleantax(os.path.abspath(fname))
        os.remove(fname)
        return rel_data, taxes

    @staticmethod
    def gen_asp_rules(relations_data, anytree_data, encoding='mnpw', reasoner='clingo'):
        get_rules_func = {'rcc': rcc_get_rules,
                          'mnpw': mnpw_get_rules}[encoding]

        rules_to_write = get_rules_func(relations_data, anytree_data)

        return rules_to_write

    @staticmethod
    def gen_asp_rules_from_cleantax(clean_tax_lines, encoding='mnpw', reasoner='clingo'):
        relation_data, anytree_data = LeanEuler.parse_cleantax(clean_tax_lines)
        return LeanEuler.gen_asp_rules(relation_data, anytree_data, encoding, reasoner)

    @staticmethod
    def visualize_input(rel_data, taxes):
        return visualize_euler_input(rel_data, taxes)

    @staticmethod
    def visualize_input_from_cleantax(cleantax_lines):
        rel_data, taxes = LeanEuler.parse_cleantax(cleantax_lines)
        return LeanEuler.visualize_input(rel_data, taxes)
