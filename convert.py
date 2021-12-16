#!/usr/bin/env python3

import csv

def write_values(the_output, row):
	the_output.write('{"')
	the_output.write("BLEPS:" + row[2])
	the_output.write('", "')
	the_output.write(row[4])
	the_output.write('", "0.5", "", "Present", "NO_ALARM", "MAJOR", "')
	the_output.write(row[5])
	the_output.write('"}\n')

with open("faults.csv") as the_data:
	with open("bleps_faults.substitutions", "w") as the_output:
	
		the_output.write('file "$(TOP)/db/bleps_bi.db"\n')
		the_output.write("{\n")
		the_output.write("pattern\n")
		the_output.write("{N                           TAG                         SCAN    ZNAM        ONAM        ZSV         OSV         DESC}\n")
		
			
		reader = csv.reader(the_data, delimiter=',', quotechar='"', skipinitialspace=True)
	
		for row in reader:
			if row[0] == 'X':
				write_values(the_output, row)
		
		the_output.write("}\n")
