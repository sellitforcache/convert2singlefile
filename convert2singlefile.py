#! /usr/bin/env python

import sys
import re

def print_in_file(outputfile,fname,linenum):
	# try to open read-in file
	try:
		readfile = open(fname,"r")
	except:
		print "Could not open read-in file '"+fname+"'. "

	#  write the file in at this line, write delimiters
	outputfile.write("c START OF BLOCK WRITTEN BY convert2singlefile.py FROM FILE "+fname+"\n")
	for line in readfile:
		outputfile.write(line)
	outputfile.write("c END OF BLOCK WRITTEN BY convert2singlefile.py FROM FILE "+fname+"\n")

	# close read-in file
	readfile.close()

	#  print statement to terminal
	print "   wrote file '"+fname+"' at line "+linenum


### get inputs
if len(sys.argv) == 1:
	print "ERROR - You must specify an input file"
	exit(0)
elif len(sys.argv) > 2:
        print "ERROR - You must specify a SINGLE input file"
        exit(0)

inputname = sys.argv[1]
outputname = inputname.split('.')[0]+"s.i"

print "Converting input "+inputname+" (and read-in files) into SINGLE FILE "+outputname+" ..."

### test input file
try:
	inputfile = open(inputname,"r")
except:
	print "Could not open file '"+inputname+"'. "

### open output file
try:
	outputfile = open(outputname,"w")
except:
	print "Could not open file '"+outputname+"' for writing. "

### make and compile regex


### scan lines, looking for 'read'
linenum = 0
for line in inputfile:
	if:
		print_in_file(outputfile,fname,linenum)
	linenum = linenum + 1


### close files, print done
inputfile.close()
outputfile.close()
print "DONE."
