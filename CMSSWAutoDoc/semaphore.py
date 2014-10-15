# altunda - ali.mehmet.altundag@cern.ch

import sys, tools.fileOps
try: import json
except ImportError: import simplejson as json

# input: release list, release, new documentetion status
if len(sys.argv) < 4:
    print >> sys.stderr, 'Error: not enough parameters.'
    sys.exit(1)

# read release list to find one to document.
relList = json.loads(tools.fileOps.read(sys.argv[1]))

print "## documentation status will be updated for %s, %s -> %s" % (sys.argv[2],
      relList[sys.argv[2]]['status'], sys.argv[3])
# update status
relList[sys.argv[2]]['status'] = sys.argv[3]

# write the updated file
tools.fileOps.write(sys.argv[1], json.dumps(relList, indent=2))
