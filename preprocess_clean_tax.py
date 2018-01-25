import sys
from sys import argv

script, fname = argv
orig_data = open(fname).readlines()

final_data = []

for i, line in enumerate(orig_data):
	if (line.strip() == '') or (line.strip()[0] == '#'):
		break
	else:
		final_data.append(line)
		
temp_data = open(fname, 'w')
temp_data.writelines(final_data)

