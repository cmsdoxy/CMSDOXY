# aaltunda - ali.mehmet.altundag@cern.ch

# this script finds an available release to generate ref man.
# please note that the output of the script should be printed
# as one line to be parsed by the sheel script.

import sys, tools.fileOps
try: import json
except ImportError: import simplejson as json

# input: releases list, label to find
if len(sys.argv) < 3:
    print >> sys.stderr, 'Error: not enough parameters.'
    sys.exit(1)

# read release list to find one to document. printFlag must be false,
# otherwise the parser in the shell script will stop execution.
rels2Doc = json.loads(tools.fileOps.read(sys.argv[1], printFlag = False))

# get keys to sort them
keys = rels2Doc.keys()
# reverse order to catch newer one (first in first out huh?)
keys.sort(reverse = True)

for i in keys:
    if rels2Doc[i]['status'] == sys.argv[2]:
        print i, rels2Doc[i]['arch']
        sys.exit(0)

# no release to document
print "-"
