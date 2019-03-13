import pandas as pd
import pickle
import numpy as np
import os

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

def get_rcc_rules():

    rcc_rules = []

    rcc_rules.append("%RCC RULES:")
    rcc_rules.append("")
    rcc_rules.append("eq(X,Y) :- eq(X,Z), eq(Z,Y).")
    rcc_rules.append("dr(X,Y) :- eq(X,Z), dr(Z,Y).")
    rcc_rules.append("pp(X,Y) :- eq(X,Z), pp(Z,Y).")
    rcc_rules.append("pi(X,Y) :- eq(X,Z), pi(Z,Y).")
    rcc_rules.append("po(X,Y) :- eq(X,Z), po(Z,Y).")

    rcc_rules.append("")
    rcc_rules.append("dr(X,Y) :- dr(X,Z), eq(Z,Y).")
    rcc_rules.append("1 {dr(X,Y) ; pp(X,Y) ; po(X,Y)} :- dr(X,Z), pp(Z,Y).")
    rcc_rules.append("1 {dr(X,Y) ; pi(X,Y) ; po(X,Y)} :- dr(X,Z), pi(Z,Y).")
    rcc_rules.append("1 {dr(X,Y) ; pp(X,Y) ; po(X,Y)} :- dr(X,Z), po(Z,Y).")

    rcc_rules.append("")
    rcc_rules.append("pp(X,Y) :- pp(X,Z), eq(Z,Y).")
    rcc_rules.append("dr(X,Y) :- pp(X,Z), dr(Z,Y).")
    rcc_rules.append("pp(X,Y) :- pp(X,Z), pp(Z,Y).")
    rcc_rules.append("dr(X,Y) ; pp(X,Y) ; po(X,Y) :- pp(X,Z), po(Z,Y).")

    rcc_rules.append("")
    rcc_rules.append("pi(X,Y) :- pi(X,Z), eq(Z,Y).")
    rcc_rules.append("1 {dr(X,Y) ; pi(X,Y) ; po(X,Y)} :- pi(X,Z), dr(Z,Y).")
    rcc_rules.append("pi(X,Y) :- pi(X,Z), pi(Z,Y).")
    rcc_rules.append("1 {pi(X,Y) ; po(X,Y)} :- pi(X,Z), po(Z,Y).")

    rcc_rules.append("")
    rcc_rules.append("po(X,Y) :- po(X,Z), eq(Z,Y).")
    rcc_rules.append("1 {dr(X,Y) ; pi(X,Y) ; po(X,Y)} :- po(X,Z), dr(Z,Y).")
    rcc_rules.append("1 {pp(X,Y) ; po(X,Y)} :- po(X,Z), pp(Z,Y).")
    rcc_rules.append("1 {dr(X,Y) ; pi(X,Y) ; po(X,Y)} :- po(X,Z), pi(Z,Y).")

    rcc_rules.append("")
    rcc_rules.append("u(X) :- dr(X,_).")
    rcc_rules.append("u(X) :- dr(_,X).")
    rcc_rules.append("u(X) :- eq(X,_).")
    rcc_rules.append("u(X) :- eq(_,X).")
    rcc_rules.append("u(X) :- po(X,_).")
    rcc_rules.append("u(X) :- po(_,X).")
    rcc_rules.append("u(X) :- pp(X,_).")
    rcc_rules.append("u(X) :- pp(_,X).")
    rcc_rules.append("u(X) :- pi(X,_).")
    rcc_rules.append("u(X) :- pi(_,X).")
    rcc_rules.append("u(X) :- bl(_,X).")
    rcc_rules.append("u(X) :- bl(X,_).")

    rcc_rules.append("")
    rcc_rules.append("eq(X,X) :- u(X).")

    rcc_rules.append("pi(X,Y) :- pp(Y,X).")
    rcc_rules.append("pp(X,Y) :- pi(Y,X).")

    rcc_rules.append("eq(X,Y) :- eq(Y,X).")
    rcc_rules.append("po(X,Y) :- po(Y,X).")
    rcc_rules.append("dr(X,Y) :- dr(Y,X).")

    rcc_rules.append("dr(Y,Z) :- bl(X,Y), bl(X,Z), Y != Z.")
    rcc_rules.append("pp(Y,X) :- bl(X,Y).")

    rcc_rules.append("")
    rcc_rules.append("1 {eq(X,Y) ; dr(X,Y) ; pp(X,Y) ; pi(X,Y) ; po(X,Y)} :- u(X), u(Y), X != Y.")

    rcc_rules.append("")
    rcc_rules.append(":- eq(X,Y), dr(X,Y).")
    rcc_rules.append(":- eq(X,Y), pp(X,Y).")
    rcc_rules.append(":- eq(X,Y), pi(X,Y).")
    rcc_rules.append(":- eq(X,Y), po(X,Y).")
    rcc_rules.append(":- dr(X,Y), pp(X,Y).")
    rcc_rules.append(":- dr(X,Y), pi(X,Y).")
    rcc_rules.append(":- dr(X,Y), po(X,Y).")
    rcc_rules.append(":- pp(X,Y), pi(X,Y).")
    rcc_rules.append(":- pp(X,Y), po(X,Y).")
    rcc_rules.append(":- pi(X,Y), po(X,Y).")

    rcc_rules.append("")

    return rcc_rules


def gen_node_name(node_name):

    return "\"{}\"".format(node_name.replace(".", "_"))


def get_rule(node1, rl, node2):

    rl_asp_dict = {PARENT : 'bl',
                   IS_INCLUDED_IN: 'pp',
                   INCLUDES: 'pi',
                   EQUALS: 'eq',
                   DISJOINT: 'dr',
                   OVERLAPS: 'po'}

    if rl in rl_asp_dict:
        return "{}({},{})".format(rl_asp_dict[rl], node1, node2)
    # print("rl {} not found".format(rl))
    return ""


def get_asp_rule(node1, rls, node2):

    # print ("Get ASP rule called with {}, {}, {}".format(node1, rls, node2))
    if len(rls) > 1:
        rules = [get_rule(node1, rl, node2) for rl in rls]
        return "1 {{ {0} }}.".format(" ; ".join(rules))
    elif len(rls) == 1:
        return "{}.".format(get_rule(node1, rls[0], node2))
    return ""


def get_rules(df, anytree_data=None):

    rules_to_write = get_rcc_rules()
    rules_to_write.append("%TAXONOMY DESC RULES\n")
    # taxonomy_dict = {}

    for index, row in df.iterrows():

        node1 = row[NODE1_COL]
        relations = row[REL_COL]
        node2 = row[NODE2_COL]

        # node1 = gen_node_name(node1) #, taxonomy_dict)
        # node2 = gen_node_name(node2) #, taxonomy_dict)

        asp_rule = get_asp_rule(node1, relations.split(","), node2)
        # print (asp_rule)
        rules_to_write.append(asp_rule)

    return rules_to_write
