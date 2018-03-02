#!/bin/sh
fname=$1
project_name=$2
python3 preprocess_clean_tax.py $1 $2
python3 cleanTax_parse.py $2
