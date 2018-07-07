import sys
from sys import argv
import argparse

OUTPUT_FOLDER = 'Preprocessed_CleanTax_Input'

def __main__():
	parser = argparse.ArgumentParser()
	parser.add_argument("fname", type = str, help = "provide the cleanTax file. It will be processed and saved in {} as $project_name.txt".format(OUTPUT_FOLDER))
	parser.add_argument("project_name", type = str, help = 'provide a suitable session/project name to reference these results in future scripts')
	args = parser.parse_args()

	fname = args.fname
	orig_data = open(fname).readlines()

	final_data = preprocess_clean_tax(orig_data)

	temp_data = open("{}/{}.txt".format(OUTPUT_FOLDER, args.project_name), 'w')
	temp_data.writelines(final_data)
	temp_data.close()

def preprocess_clean_tax(clean_tax_lines):

	def is_an_empty_line(line):
		return line.strip() == ''
	def is_a_comment(line):
		return line.strip()[0] == '#'

	preprocessed_data = [line for line in clean_tax_lines if (not is_an_empty_line(line)) and (not is_a_comment(line))]
	return preprocessed_data

if __name__ == '__main__':
	__main__()

