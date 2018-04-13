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

def gen_node_name(node_name: str):

	return "\"{}\"".format(node_name.replace(".", "_"))

def gen_isa_rule(n1: str, n2: str, idx: int):

	r1 = "ir(X, r{}) :- in({}, X), out({}, X).".format(idx, n1, n2)
	r2 = ":- #count {{X : vrs(X), in({}, X), in({}, X)}} <= 0.".format(n1, n2)
	return "\n".join([r1,r2])

def gen_coverage_rule(parent: str, children: list):

	lhs = 'out({}, X)'.format(parent)
	rhs = ", ".join(list(map(lambda x: 'out({}, X)'.format(x), children)))

	return "{} :- {}.".format(lhs, rhs)

def gen_sibling_disjointness(n1: str, n2: str, idx: int):

	def in_out_helper(nn1, nn2):
		return ":- #count {{X : vrs(X), in({}, X), out({}, X)}} <= 0.".format(nn1, nn2)

	r1 = "ir(X, r{}) :- in({}, X), in({}, X).".format(idx, n1, n2)
	r2 = in_out_helper(n1, n2)
	r3 = in_out_helper(n2, n1)

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





