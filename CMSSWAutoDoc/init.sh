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
export LOG=$LOG_PATH/$(date +%Y%m%d_%H%M).log

if [ ! -d "$LOG_PATH" ]; then
    mkdir $LOG_PATH
fi

if [ ! -d "$TMP" ]; then
    mkdir $TMP
fi
