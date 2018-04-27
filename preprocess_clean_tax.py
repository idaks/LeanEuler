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

	final_data = []

	for i, line in enumerate(orig_data):
		if (line.strip() == '') or (line.strip()[0] == '#'):
			continue
		else:
			final_data.append(line)

	temp_data = open("{}/{}.txt".format(OUTPUT_FOLDER, args.project_name), 'w')
	temp_data.writelines(final_data)
	temp_data.close()

if __name__ == '__main__':
	__main__()

