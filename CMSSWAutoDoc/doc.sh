#!/bin/bash

# if you get negative (!=0) result from the last command,
# print the error message and exit
function checkError(){
    if [ $(echo $?) -ne 0 ]; then
        echo "ERROR: $1"
        exit 1
    fi
}

WORK_DIR=$(pwd)
BASE=$(dirname $(readlink -f "${BASH_SOURCE[0]}"))
cd $BASE
source init.sh

OUTPUT=$(python find.py $IOFILE)
checkError "find.py didn't return zero."

# get version of the CMSSW
REL=$(echo $OUTPUT | cut -f 1 -d ' ')
# get destination architexture
ARCH=$(echo $OUTPUT | cut -f 2 -d ' ')

echo "Documenting $REL ($ARCH)..."

# set the architecture
export SCRAM_ARCH=$ARCH
cd $TMP

# create the CMSSW base
#cmsrel $REL # huh?
scramv1 project CMSSW $REL
checkError "CMSSW could not be initialized properly."
cd $REL

# set the cms env
#cmsenv # huh?
eval `scramv1 runtime -sh`
checkError "CMSSW environments could not be set."

# clone CMSSW repo
git clone https://github.com/cms-sw/cmssw.git src
checkError "Repo could not be cloned."
cd src/
git checkout $REL
cd ..


# clean up the base
cd $TMP/$REL
rm -rf biglib/ bin/ cfipython/ config/ include/ lib/ logs/ objs/ python/ src/ test/ tmp/
gzip -r -S gz doc/
echo 'auto-generated' > out.txt

cd $WORK_DIR
