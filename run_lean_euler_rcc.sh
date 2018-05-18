#!/bin/bash

CLEAN_TAX_FILE=$1
PROJECT_NAME=$2

#Preprocess the clean tax file to make it suitable for parsing. Stores the preprocessed file in the Preprocessed_CleanTax_Input directory as $PROJECT_NAME.txt
python3 preprocess_clean_tax.py $CLEAN_TAX_FILE $PROJECT_NAME

#Parse the cleantax file and generate the Pandas dataframes that hold the relevant information to generate clingo/ASP files.
python3 cleanTax_parse.py $PROJECT_NAME

#Generate the clingo file for the provided taxonomy alignment problem. Stores the generated clingo file in Clingo_Input_Files directory as $PROJECT_NAME.lp4
python3 generate_ASP.py -encoding rcc $PROJECT_NAME