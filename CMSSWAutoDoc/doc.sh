#!/bin/bash

WORK_DIR=$(pwd)
BASE=$(dirname $(readlink -f "${BASH_SOURCE[0]}"))
cd $BASE
source init.sh

echo $TMP

OUTPUT=$(python find.py $IOFILE)
REL=$(echo $OUTPUT | cut -f 1 -d ' ')
ARCH=$(echo $OUTPUT | cut -f 2 -d ' ')

echo "Documenting $REL ($ARCH)..." #>> $LOG

# set the architecture
export SCRAM_ARCH=$ARCH
cd $TMP

# create the CMSSW base
#cmsrel $REL # huh?
scramv1 project CMSSW $REL
cd $REL

# set the cms env
#cmsenv # huh?
eval `scramv1 runtime -sh`

# clone CMSSW repo
git clone https://github.com/cms-sw/cmssw.git src
cd src/
git checkout $REL
cd ..


# clean up the base
cd $TMP/$REL
rm -rf biglib/ bin/ cfipython/ config/ include/ lib/ logs/ objs/ python/ src/ test/ tmp/
gzip -r -S gz doc/
echo 'auto-generated' > out.txt

cd $WORK_DIR
