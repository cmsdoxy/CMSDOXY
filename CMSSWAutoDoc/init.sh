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

# Redirect stdout ( > ) into a named pipe ( >() ) running "tee"
exec > >(tee -a "${LOG_PATH}/${LOG_DATE}.log")
# capture stderr
exec 2>&1
