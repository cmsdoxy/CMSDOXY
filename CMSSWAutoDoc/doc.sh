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

OUTPUT=$(python find.py $IOFILE "undocumented")
checkError "find.py didn't return zero."

if [ "-" == "$OUTPUT" ]; then
    echo "## nothing to document... Cool huh?"
    echo ""
    exit 0
fi

# get version of the CMSSW
REL=$(echo $OUTPUT | cut -f 1 -d ' ')
# get destination architexture
ARCH=$(echo $OUTPUT | cut -f 2 -d ' ')

python semaphore.py $IOFILE $REL "documenting.."
checkError "$IOFILE could not be updated."

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

######## HARD CODED DOCKIT SECTION ########
cp -r /afs/cern.ch/work/c/cmsdoxy/DocKit .
cd DocKit/scripts
tcsh generate_reference_manual
# add check point here!
######## HARD CODED DOCKIT SECTION ########

# clean up the base
cd $TMP/$REL
rm -rf biglib/ bin/ cfipython/ config/ include/ lib/ logs/ objs/ python/ src/ test/ tmp/ DocKit/
gzip -r -S gz doc/
echo 'auto-generated' > out.txt

cd $BASE
python semaphore.py $IOFILE $REL "documented"
checkError "$IOFILE could not be updated."

cd $WORK_DIR

echo "## document for $REL has been created."
echo ""
