#!/bin/bash

# get the scram
shopt -s expand_aliases
source /cvmfs/cms.cern.ch/cmsset_default.sh

# if you get negative (!=0) result from the last command,
# print the error message and exit
function checkError(){
    if [ $(echo $?) -ne 0 ]; then
        echo "ERROR: $1"
        # try to unlock the release. you might get an error once again
        # message if the caller error semaphore script based problem
        python $BASE/semaphore.py $IOFILE $REL "undocumented"
        exit 1
    fi
}

WORK_DIR=$(pwd)
BASE=$(dirname $(readlink -f "${BASH_SOURCE[0]}"))
cd $BASE
source init.sh

RELEASE=$(python $BASE/find.py $IOFILE "undocumented")
checkError "find.py didn't return zero."

if [ "-" == "$RELEASE" ]; then
    echo "## nothing to document... Cool huh?"
    echo ""
    exit 0
fi

# get version of the CMSSW
REL=$(echo $RELEASE | cut -f 1 -d ' ')
# get destination architexture
ARCH=$(echo $RELEASE | cut -f 2 -d ' ')

# Redirect stdout ( > ) into a named pipe ( >() ) running "tee"
exec > >(tee -a "${LOG_PATH}/${REL}_${LOG_DATE}.log")
# capture stderr
exec 2>&1

echo "## hostname: $(hostname)"
echo "## user:     $(whoami)"
echo "## Documenting $REL ($ARCH)..."

python $BASE/semaphore.py $IOFILE $REL "documenting..."
checkError "$IOFILE could not be updated."

# set the architecture
export SCRAM_ARCH=$ARCH
cd $TMP

# delete old release direcroy in case of an unsuccessful doc process if exists
if [ -d "$TMP/$REL" ]; then
    echo "## I saw that the $REL is already there! I will delete it now."
    rm -rf $TMP/$REL
fi

# create the CMSSW base
cmsrel $REL # huh?
#scramv1 project CMSSW $REL
checkError "CMSSW could not be initialized properly."
cd $TMP/$REL

# set the cms env
cmsenv # huh?
#eval `scramv1 runtime -sh`
checkError "CMSSW environments could not be set."

# clone CMSSW repo
git clone https://github.com/cms-sw/cmssw.git src
checkError "Repo could not be cloned."
cd $TMP/$REL/src/
git checkout $REL
cd $TMP/$REL

######## HARD CODED DOCKIT SECTION ########
cd $TMP/$REL/src/Documentation/
echo "go to: $TMP/$REL/src/Documentation/"
rm -rf ReferenceManualScripts/
echo "delete: ReferenceManualScripts"
cp -r /afs/cern.ch/work/c/cmsdoxy/ReferenceManualScripts .
checkError "I coldn't copy the directory, /afs/cern.ch/work/c/cmsdoxy/ReferenceManualScripts"
echo "cp -r /afs/cern.ch/work/c/cmsdoxy/ReferenceManualScripts `pwd`"
cd $TMP/$REL/src/Documentation/ReferenceManualScripts/scripts
tcsh generate_reference_manual
# add check point here!
######## HARD CODED DOCKIT SECTION ########

# clean up the base
cd $TMP/$REL
rm -rf biglib/ bin/ cfipython/ config/ include/ lib/ logs/ objs/ python/ src/ test/ tmp/ DocKit/
gzip -r -S gz doc/
echo "generated on $(date)" > auto.doc.2

cd $BASE
python $BASE/semaphore.py $IOFILE $REL "documented"
checkError "$IOFILE could not be updated."

# upload ref man files (hardcoded username & machine!)
echo "## uploading files..."
scp -r $TMP/$REL cmsdoxy@cmssdt01.cern.ch:/data/doxygen > /dev/null
checkError "auto-generated documentation could not be uploaded."

cd $WORK_DIR

echo "## document for $REL has been created."
echo ""
