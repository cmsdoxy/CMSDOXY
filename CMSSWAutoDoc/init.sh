#!/bin/bash

BASE=$(dirname $(readlink -f "${BASH_SOURCE[0]}"))
cd $BASE/..
source init.sh
cd $BASE

export NAME=CMSSWAutoDoc
export CONFIG=$DATA/$NAME/conf.json
export TMP=$TMP/$NAME
export IOFILE=$TMP/cmsswRels2Doc.json
export LOG_PATH=$LOGS/$NAME
export LOG_DATE=$(date +%Y%m%d_%H%M)

if [ ! -d "$LOG_PATH" ]; then
    mkdir $LOG_PATH
fi

if [ ! -d "$TMP" ]; then
    mkdir $TMP
fi

# check for quota
QUOTA=$(fs lq $BASE)
QNAME=$(echo $QUOTA | cut -f 7 -d ' ')
QRATE=$(echo $QUOTA | cut -f 10 -d ' ' | cut -d "%" -f1)
echo "## Quota base: $BASE"
echo "## Quota name: $QNAME"
echo "## Quota rate: $QRATE"
if [ $QRATE -gt "70" ]; then
   echo "quota exceeded (threshold: 70%)!"
   exit 1
fi
