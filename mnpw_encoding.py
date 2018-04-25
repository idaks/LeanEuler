#!/usr/bin/env python3
import argparse
import pandas as pd
import pickle
import numpy as np
import os
from helper import lineno, isfloat, mkdir_p, get_rcc_rules

#EDGE_TYPES
PARENT = "parent"
IS_INCLUDED_IN = "<"
INCLUDES = ">"
EQUALS = "="
DISJOINT = "!"
OVERLAPS = "o"

rl = {
	"=": int('010', 2),
	"o": int('111', 2),
	""
}

def gen_node_name(node_name: str):

	return "\"{}\"".format(node_name.replace(".", "_"))

def count_non_zero(t1: str, t2: str, n1: str, n2: str):

	return ":- #count {{X : vrs(X), {}({}, X), {}({}, X)}} <= 0.".format(t1, nn1, t2, nn2)

def count_non_zero_in_out(nn1: str, nn2: str):

	return count_non_zero("in", "out", nn1, nn2)

def count_nonzero_in_in(nn1: str, nn2: str):

	return count_non_zero("in", "in", nn1, nn2)

def count_nonzero_out_out(nn1: str, nn2: str):

	return count_non_zero("out", "out", nn1, nn2)

def count_nonzero_out_in(nn1: str, nn2: str):

	return count_non_zero_in_out(nn2, nn1)

def ir_helper(t1: str, t2: str, n1: str, n2: str, idx: int):

	return "ir(X, r{}) :- {}({}, X), {}({}, X).".format(idx, t1, n1, t2, n2)

def ir_in_out(n1: str, n2: str, idx: int):

	return ir_helper("in", "out", n1, n2, idx)

def ir_in_in(n1: str, n2: str, idx: int):

	return ir_helper("in", "in", n1, n2, idx)

def ir_out_out(n1: str, n2: str, idx: int):

	return ir_helper("out", "out", n1, n2, idx)

def ir_out_in(n1: str, n2: str, idx: int):

	return ir_in_out(n2, n1, idx)

def gen_isa_rule(n1: str, n2: str, idx: int):

	r1 = ir_in_out(n1, n2, idx) #"ir(X, r{}) :- in({}, X), out({}, X).".format(idx, n1, n2)
	r2 = count_non_zero_in_in(n1, n2) #":- #count {{X : vrs(X), in({}, X), in({}, X)}} <= 0.".format(n1, n2)
	return "\n".join([r1,r2])

def gen_coverage_rule(parent: str, children: list):

	lhs = 'out({}, X)'.format(parent)
	rhs = ", ".join(list(map(lambda x: 'out({}, X)'.format(x), children)))

	return "{} :- {}.".format(lhs, rhs)

def gen_sibling_disjointness(n1: str, n2: str, idx: int):

	r1 = ir_in_in(n1, n2, idx) #"ir(X, r{}) :- in({}, X), in({}, X).".format(idx, n1, n2)
	r2 = count_nonzero_in_out(n1, n2)
	r3 = count_nonzero_in_out(n2, n1)

	return "\n".join([r1,r2,r3])

def gen_region_constraints():

	irs = "irs(X) :- ir(X, _)."
	vrs = "vrs(X) :- vr(X, _)."
	vr = "vr(X, X) :- not irs(X), r(X)."
	ir = "ir(X, X) :- not vrs(X), r(X)."
	exactly_one = ":- vrs(X), irs(X)."

	return "\n".join([irs, vrs, vr, ir, exactly_one])

def gen_euler_bit():

	r1 = "bit(M, {}, V) :- r(M), M1=M/1, V = M1 \ 5.".format(0)
	r2 = "bit(M, {}, V) :- r(M), M1=M/1, V = M1 \ 5.".format(1)

def gen_region_meanings():

	in_rule =   "in(X, M) :- r(M), concept(X, T, N), N1=N+1, bit(M, T, N1)."
	out_rule = "out(X, M) :- r(M), concept(X, T, N), N1=N+1, not bit(M, T, N1)."
	exactly_one = "in(X, M) :- r(M), concept2(X, _), not out(X, M)."
	irs_rule = "irs(M) :- in(X, M), out(X, M), r(M), concept2(X, _)."

	return "\n".join([in_rule, out_rule, exactly_one, irs_rule])

def gen_congruence_rel(n1: str, n2: str, idx: int):

	r1 = ir_out_in(n1, n2, idx) #"ir(X, r{}) :- out({}, X), in({}, X).".format(idx, n1, n2)
	r2 = ir_out_in(n2, n1, idx) #"ir(X, r{}) :- out({}, X), in({}, X).".format(idx, n2, n1)
	r3 = count_non_zero_in_in(n1, n2) #":- #count{{X : vrs(X), in({}, X), in({}, X)}} <= 0.".format(n1, n2)

	return "\n".join([r1, r2, r3])

def gen_proper_part_rel(n1: str, n2: str, idx: int):

	r1 = ir_in_out(n1, n2, idx) #"ir(X, r{}) :- in({}, X), out({}, X).".format(idx, n1, n2)
	r2 = count_non_zero_in_in(n1, n2) #":- #count{{X : vrs(X), in({}, X), in({}, X)}} = 0.".format(n1, n2)
	r3 = count_non_zero_out_in(n1, n2) #":- #count{{X : vrs(X), out({}, X), in({}, X)}} = 0.".format(n1, n2)

	return "\n".join([r1, r2, r3])

def gen_proper_part_reverse_rel(n1: str, n2: str, idx: int):

	r1 = ir_out_in(n1, n2, idx) #"ir(X, r{}) :- out({}, X), in({}, X).".format(idx, n1, n2)
	r2 = count_non_zero_in_out(n1, n2) #":- #count{{X : vrs(X), in({}, X), out({}, X)}} = 0.".format(n1, n2)
	r3 = count_non_zero_in_in(n1, n2) #":- #count{{X : vrs(X), in({}, X), in({}, X)}} = 0.".format(n1, n2)

	return "\n".join([r1, r2, r3])

def gen_partial_overlap_rel(n1: str, n2: str):

	r1 = count_non_zero_in_out(n1, n2) #":- #count{{X : vrs(X), in({}, X), out({}, X)}} = 0.".format(n1, n2)
	r2 = count_non_zero_in_in(n1, n2) #":- #count{{X : vrs(X), in({}, X), in({}, X)}} = 0.".format(n1, n2)
	r3 = count_non_zero_out_in(n1, n2) #":- #count{{X : vrs(X), out({}, X), in({}, X)}} = 0.".format(n1, n2)

	return "\n".join([r1, r2, r3])

def gen_disjoint_rel(n1: str, n2: str, idx: int)

	r1 = count_non_zero_in_out(n1, n2)
	r2 = ir_in_in(n1, n2, idx)
	r3 = count_non_zero_out_in(n1, n2)

	return "\n".join([r1, r2, r3])




