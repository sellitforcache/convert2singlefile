#! /usr/bin/env python

import sys

if len(sys.argv) == 1:
	print "ERROR - You must specify an input file"
	exit(0)
elif len(sys.argv) > 2:
        print "ERROR - You must specify a SINGLE input file"
        exit(0)

input = sys.argv[1]
output = input.split('.')[0]+"s.i"

print "Converting input "+input+" (and read-in files) into SINGLE FILE "+output+" ..."



print "DONE."
