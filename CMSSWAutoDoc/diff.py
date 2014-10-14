# aaltunda- ali.mehmet.altundag@cern.ch

import os, sys, re
import tools.url, tools.fileOps
try: import json
except ImportError: import simplejson as json
try: import xml.etree.ElementTree as ET
except ImportError: from elementtree import ElementTree as ET

# Input: config file, input, output
if len(sys.argv) < 2:
    print >> sys.stderr, 'ERROR: config file couldn\'t be found.'
    sys.exit(1)

# read the config file and parse it
conf     = json.loads(tools.fileOps.read(sys.argv[1]))

# get list of announced cmssw releases and parse it
cmssw    = ET.fromstring(tools.url.read(conf['urlRelList']))
# get list of documented cmssw releases and parse it
docCMSSW = ET.fromstring(tools.url.read(conf['urlDocList']))

def isDocNeeded(relName):
    if re.match(conf['pattern'], relName): return True
    else: return False

# cmssw XML structure
class CMSSW:
    def __init__(self, name = None, arch = None, type = None,
                 state = None):
        self.name     = name.strip()
        self.arch     = arch
        self.type     = type
        self.state    = state

    # for string type casting
    def __str__(self):
        return "%s, %s, %s, %s" % (self.name, self.arch, self.type, self.state)

    # overload the equality operator in order to be able to use operator 'in'
    def __eq__(self, b):
        if b.name == self.name: return True
        return False

# please see the related xml file structure
cmsswArray = []
for archNode in cmssw.findall('architecture'):
    arch = archNode.attrib['name']
    for projectNode in archNode.findall('project'):
        name  = projectNode.attrib['label']
        type  = projectNode.attrib['type']
        state = projectNode.attrib['state']
        cmsswArray.append(CMSSW(name, arch, type, state))

# please see the related xml file structure
cmsswDocArray = []
for projectNode in docCMSSW.findall('project'):
    name =  projectNode.attrib['label']
    # append the release if it is documented (in short, eliminate deprecated releases)
    if projectNode.attrib['url'] != '':
        cmsswDocArray.append(CMSSW(name = name))

diff = {}
for i in cmsswArray:
    # append undocumented relaease if it is matching with the pattern
    # this patter is used for skipping special releases which we don't
    # need to document. Note that, someone might want you to generate
    # documentation for this special release. In that case, you will
    # need to generate it by hand.
    if not i in cmsswDocArray and isDocNeeded(i.name):
        # make it easy to parse
        diff[i.name] = {'status' : 'undocumented', 'arch':i.arch}

try:
    # try to read & parse input file which is old diff file
    oldDiff = json.loads(tools.fileOps.read(sys.argv[2]))
except IOError:
    # file not found, that means this is the first time
    # that the script has been run
    oldDiff = {}

# update the diff file
for i in diff:
    if not i in oldDiff: oldDiff[i] = diff[i]

# updated diff
out = json.dumps(oldDiff, indent=2)
print out
tools.fileOps.write(sys.argv[2], out)

sys.exit(0)
