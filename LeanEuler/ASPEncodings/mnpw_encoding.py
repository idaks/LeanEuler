#!/usr/bin/env python3
import anytree
import numpy as np
import pandas as pd

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

equals = np.array([0,1,0], dtype="bool")
overlaps = np.array([1,1,1], dtype="bool")
included_in = np.array([0,1,1], dtype="bool")
disjoint = np.array([1,0,1], dtype="bool")
includes = np.array([1,1,0], dtype="bool")

sym_dict = {
    "=": equals,
    "o": overlaps,
    "<": included_in,
    ">": includes,
    "!": disjoint
}

all_rels = set(sym_dict.keys())

idx_rel_map = {0: ("in", "out"),
               1: ("in", "in"),
               2: ("out", "in")}


def rec_bitwise_and(fs):
    if len(fs) == 1:
        return fs[0]
    if len(fs) == 2:
        return np.bitwise_and(fs[0], fs[1])
    mid = int(np.ceil(len(fs)/2))
    return np.bitwise_and(rec_bitwise_and(fs[:mid]), rec_bitwise_and(fs[mid:]))


def rec_bitwise_and_not(fs):
    f_not = list(map(np.invert, fs))
    return rec_bitwise_and(f_not)


def intersection(fs):
    t1 = rec_bitwise_and(fs)
    t2 = rec_bitwise_and_not(fs)
    return np.bitwise_or(t1, t2)


def not_filter_helper(r_var, rel1, rel2, n1, n2, sign):
    return "#count {{{0} : vrs({0}), {1}({3}, {0}), {2}({4}, {0})}} {5} 0".format(r_var, rel1, rel2, n1, n2, sign)


def not_filter(n1, n2, rel):
    ts = []
    for i in range(len(rel)):
        t = not_filter_helper(chr(ord('A')+i), idx_rel_map[i][0], idx_rel_map[i][1], n1, n2, ">" if rel[i] else "=")
        ts.append(t)
    return ":- {}.".format(",\n   ".join(ts))


def ir_helper(rel1: str, rel2: str, n1: str, n2: str, idx: int, rel_var="X"):
    return "ir({0}, r{1}) :- {2}({3}, {0}), {4}({5}, {0}).".format(rel_var, idx, rel1, n1, rel2, n2)


def vr_ir_helper(rel1: str, rel2: str, n1: str, n2: str, idx: int, rel_var="X"):
    return "vr({}, r{}) ; ".format(rel_var, idx) + ir_helper(rel1, rel2, n1, n2, idx, rel_var)


def gen_coverage_rule(parent: str, children: list):  # For every non-leaf node
    header = '% Coverage for {}'.format(parent)
    lhs = 'out({}, X)'.format(parent)
    rhs = ", ".join(list(map(lambda x: 'out({}, X)'.format(x), children)))
    return "{}\n{} :- {}.\n".format(header, lhs, rhs)


def gen_concept2_rule(node: str, tax_num: int):
    return "concept2({}, {}).".format(node, tax_num)


def gen_concept_rule(node: str, tax_num: int, concept_num: int):
    return "concept({}, {}, {}).".format(node, tax_num, concept_num)


def concept2_concept_rel():
    return "concept2(A, B) :- concept(A,B,_)."


def gen_sibling_disjointness(n1: str, n2: str, idx: int):  # For every pair of siblings
    header = '% {} ! {}'.format(n1, n2)
    r1 = ir_helper(n1=n1, n2=n2, rel1="in", rel2="in", idx=idx)
    r2 = ":- {}.".format(not_filter_helper(n1=n1, n2=n2, rel1="in", rel2="out", sign="=", r_var="X"))
    r3 = ":- {}.".format(not_filter_helper(n1=n2, n2=n1, rel1="in", rel2="out", sign="=", r_var="X"))
    return "\n".join([header, r1,r2,r3, ''])


def gen_isa_rule(child: str, parent: str, idx: int):  # For every parent-child relation
    header = '% {} isa {}'.format(child, parent)
    r1 = ir_helper(n1=child, n2=parent, rel1="in", rel2="out", idx=idx)
    r2 = ":- {}.".format(not_filter_helper(n1=child, n2=parent, rel1="in", rel2="in", sign="=", r_var="X"))
    return "\n".join([header, r1,r2, ''])


def gen_euler_bit(tax_id, prod, count):  # Standard
    header = '%  Euler Bit'
    r1 = "bit(M, {}, V) :- r(M), M1=M/{}, V = M1 \ {}.".format(tax_id, prod, count)
    return [header, r1, '']


def gen_region_meanings():  # Standard
    header = "% Region Meanings"
    in_rule =   "in(X, M) :- r(M), concept(X, T, N), N1=N+1, bit(M, T, N1)."
    out_rule = "out(X, M) :- r(M), concept(X, T, N), N1=N+1, not bit(M, T, N1)."
    exactly_one = "in(X, M) :- r(M), concept2(X, _), not out(X, M)."
    irs_rule = "irs(M) :- in(X, M), out(X, M), r(M), concept2(X, _)."
    return [header, in_rule, out_rule, exactly_one, irs_rule, '']


def gen_region_constraints():  # Standard
    header = "% Region Constraints"
    irs = "irs(X) :- ir(X, _)."
    vrs = "vrs(X) :- vr(X, _)."
    vr = "vr(X, X) :- not irs(X), r(X)."
    ir = "ir(X, X) :- not vrs(X), r(X)."
    exactly_one = ":- vrs(X), irs(X)."
    return [header, irs, vrs, vr, ir, exactly_one, '']


def gen_bl_rules(parent, children):
    return ['bl({}, {}).'.format(parent, child) for child in children]


def euler_region_count(end, start=1):
    return ["r({}..{}).".format(start, end), '']


rule_count = 0  # POTENTIAL BUG!


def initial_rules(num_regions):
    global rule_count
    euler_region_count_rule = euler_region_count(num_regions)
    # euler_bit_rules = gen_euler_bit()
    region_meaning_rules = gen_region_meanings()
    region_constraint_rules = gen_region_constraints()
    concept2_concept_rule = concept2_concept_rel()
    all_rules = euler_region_count_rule
    # all_rules.extend(euler_bit_rules)
    all_rules.extend(region_meaning_rules)
    all_rules.extend(region_constraint_rules)
    all_rules.append(concept2_concept_rule)
    return all_rules


def gen_tax_rules(root, tax_id=0, concept_count=0):
    global rule_count
    children = root.children
    sd_r = []
    cov_r = []
    concept_r = []
    isa_r = []
    bl_rules = []
    if len(children) > 0:
        for n1 in range(len(children)):
            for n2 in range(n1+1, len(children)):
                sd_r.append(gen_sibling_disjointness(children[n1].name, children[n2].name, rule_count))
                rule_count += 1
        cov_r.extend([gen_coverage_rule(root.name, list(map(lambda x: x.name, children)))])
        bl_rules.extend(gen_bl_rules(root.name, list(map(lambda x: x.name, children))))
        concept_r.extend([gen_concept2_rule(root.name, tax_id)])
        for child in children:
            isa_r.append(gen_isa_rule(child.name, root.name, rule_count))
            rule_count += 1
        for child in children:
            t_sd_r, t_cov_r, t_concept_r, t_isa_r, t_bl_rules, concept_count = gen_tax_rules(child, tax_id, concept_count)
            sd_r.extend(t_sd_r)
            cov_r.extend(t_cov_r)
            concept_r.extend(t_concept_r)
            isa_r.extend(t_isa_r)
            bl_rules.extend(t_bl_rules)
    else:
        concept_r = [gen_concept_rule(root.name, tax_id, concept_count)]
        concept_count += 1
    return sd_r, cov_r, concept_r, isa_r, bl_rules, concept_count


def gen_rules(n1, n2, rels):
    """
    Generates the rules that must be encoded in clingo to represent the
    list of possible relations (rels) between given nodes n1 and n2
    """
    global rule_count
    update_rule_count = False

    rules = ['% {} {} {}'.format(n1, rels, n2)]
    not_rels = list(all_rels - set(rels))
    rels = list(map(lambda x: sym_dict[x], rels))
    not_rels = list(map(lambda x: sym_dict[x], not_rels))
    for not_rel in not_rels:
        rules.append(not_filter(n1, n2, not_rel))
    if len(rels) > 1:
        intersect = intersection(rels)
        for i in range(len(intersect)):
            if intersect[i] == 1 and rels[0][i] == 0:
                rules.append(ir_helper(idx_rel_map[i][0], idx_rel_map[i][1], n1, n2, rule_count))
                update_rule_count = True
            elif intersect[i] == 1 and rels[0][i] == 1:
                rules.append(":- {}.".format(not_filter_helper("X", idx_rel_map[i][0], idx_rel_map[i][1], n1, n2, "="), "."))
            elif intersect[i] == 0:
                rules.append(vr_ir_helper(idx_rel_map[i][0], idx_rel_map[i][1], n1, n2, rule_count))
                update_rule_count = True
    else:
        for i in range(len(rels[0])):
            if rels[0][i] == 0:
                rules.append(ir_helper(idx_rel_map[i][0], idx_rel_map[i][1], n1, n2, rule_count))
                update_rule_count = True
            elif rels[0][i] == 1:
                rules.append(":- {}.".format(not_filter_helper("X", idx_rel_map[i][0], idx_rel_map[i][1], n1, n2, "="), "."))

    if update_rule_count:
        rule_count += 1

    rules.append('')

    return rules


def decoding_rules():

    rel_list = list(all_rels)
    mir_rules = ['% Decoding Rules']  # I DONT REMEMBER WHY I PUT THIS HERE
    for i in range(len(rel_list)):
        for j in range(i+1, len(rel_list)):
            mir_rules.append(':- rel(X, Y, "{}"), rel(X, Y, "{}"), concept2(X, N1), concept2(Y, N2).'.format(rel_list[i], rel_list[j]))

    mir_rules.append('')

    t = []
    for rel in rel_list:
        t.append('not rel(X, Y, "{}")'.format(rel))
    t.append('concept2(X, N1)')
    t.append('concept2(Y, N2)')
    t.append('N1 < N2')
    at_least_one_rule = ':- {}.\n'.format(", ".join(t))  # I DONT REMEMBER WHY I PUT THIS HERE

    rel_def = []  # I DONT REMEMBER WHY I PUT THIS HERE
    for rel in rel_list:
        t_ = []
        for i in range(3):
            t_.append('{1}hint(X, Y, {0})'.format(i, "" if sym_dict[rel][i] else "not "))
        rel_def.append('rel(X, Y, "{}") :- {}.'.format(rel, ", ".join(t_)))

    rel_def.append('')

    hint_def = []  # I DONT REMEMBER WHY I PUT THIS HERE
    for i in range(3):
        hint_def.append('hint(X, Y, {}) :- concept2(X, N1), concept2(Y, N2), N1 < N2, vrs(R), {}(X, R), {}(Y, R).'
                        .format(i, idx_rel_map[i][0], idx_rel_map[i][1]))

    all_rules = mir_rules
    all_rules.append(at_least_one_rule)
    all_rules.extend(rel_def)
    all_rules.extend(hint_def)
    all_rules.append('')
    return all_rules


def final_filter(show_rel=True, rcc_conversion=True):

    filter_rules = []
    if show_rel:
        filter_rules.append('#show rel/3.')
    if rcc_conversion:
        filter_rules.append('eq(A, B) :- rel(A, B, "=").')
        filter_rules.append('po(A, B) :- rel(A, B, "o").')
        filter_rules.append('dr(A, B) :- rel(A, B, "!").')
        filter_rules.append('pp(A, B) :- rel(A, B, "<").')
        filter_rules.append('pp(B, A) :- rel(A, B, ">").')
        filter_rules.append("pp(Y,X) :- bl(X,Y).")
        filter_rules.append("u(X) :- bl(_,X).")
        filter_rules.append("u(X) :- bl(X,_).")
        # filter_rules.append("u(X) :- dr(X,_).")
        # filter_rules.append("u(X) :- dr(_,X).")
        # filter_rules.append("u(X) :- eq(X,_).")
        # filter_rules.append("u(X) :- eq(_,X).")
        # filter_rules.append("u(X) :- po(X,_).")
        # filter_rules.append("u(X) :- po(_,X).")
        # filter_rules.append("u(X) :- pp(X,_).")
        # filter_rules.append("u(X) :- pp(_,X).")
        # filter_rules.append("u(X) :- pi(X,_).")
        # filter_rules.append("u(X) :- pi(_,X).")
        filter_rules.append('#show eq/2.')
        filter_rules.append('#show po/2.')
        filter_rules.append('#show pp/2.')
        # filter_rules.append('#show pi/2.')
        filter_rules.append('#show dr/2.')
        filter_rules.append('#show bl/2.')
        filter_rules.append('#show u/1.')

    return filter_rules


def get_rules(articulations, anytree_):

    rules_to_write = []

    sibling_disjointness_rules = []
    coverage_rules = []
    concept_rules = []
    isa_rules = []
    euler_bit_rules = []
    bl_rules = []

    num_regions = 0
    prod = 1
    for i, tax_name in enumerate(anytree_.keys()):
        root = anytree_[tax_name][tax_name].children[0]
        all_rules = gen_tax_rules(root, tax_id=i)
        n_concepts = all_rules[5]
        euler_bit_rules.extend(gen_euler_bit(i, prod, n_concepts+1))
        prod *= (n_concepts + 1)
        num_regions = (num_regions * n_concepts) + num_regions + n_concepts
        sibling_disjointness_rules.extend(all_rules[0])
        coverage_rules.extend(all_rules[1])
        concept_rules.extend(all_rules[2])
        isa_rules.extend(all_rules[3])
        bl_rules.extend(all_rules[4])

    articulation_rules = ['% Articulations', '']
    for idx, row in articulations.iterrows():
        n1 = row[NODE1_COL]
        rel = row[REL_COL].split(",")
        n2 = row[NODE2_COL]
        if rel[0] != PARENT:
            articulation_rules.extend(gen_rules(n1, n2, rel))

    decoding_rules_ = decoding_rules()
    init_rules = initial_rules(num_regions=num_regions)

    rules_to_write.extend(init_rules)
    rules_to_write.append('')
    rules_to_write.append('% Taxonomy Description\n')
    rules_to_write.extend(euler_bit_rules)
    rules_to_write.extend(concept_rules)
    rules_to_write.append('')
    rules_to_write.extend(isa_rules)
    rules_to_write.extend(coverage_rules)
    rules_to_write.extend(sibling_disjointness_rules)
    rules_to_write.extend(articulation_rules)
    rules_to_write.extend(decoding_rules_)
    rules_to_write.append('\n% Child Parent Rules for Viz\n')
    rules_to_write.extend(bl_rules)
    rules_to_write.append('')
    rules_to_write.extend(final_filter())

    return rules_to_write
