#!/bin/sh
fname=$1
pytho3preprocess_clean_tax.py $1
./cleanTax_parse.py $1
