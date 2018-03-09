import errno
import inspect
import sys
from sys import argv
import string
import os


###################################################################

#to help debug
def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno

###################################################################

###################################################################

#helper funcs

def isfloat(value):
  """returns true if a value can be typecasted as a float, else false"""
  try:
    float(value)
    return True
  except ValueError:
    return False

def mkdir_p(path):
    """make a directory if it doesn't already exist"""
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

###################################################################

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

####################################################################################################################


####################################################################################################################
