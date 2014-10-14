#!/bin/bash

BASE=$(dirname $(readlink -f "${BASH_SOURCE[0]}"))
cd $BASE/..
source init.sh
cd $BASE

NAME=CMSSWAutoDoc
CONFIG=$DATA/$NAME/conf.json
IOFILE=$TMP/cmsswRels2Doc.json
LOG_PATH=$LOGS/$NAME
LOG=$LOG_PATH/$(date +%Y%m%d_%H%M).log

if [ ! -d "$LOG_PATH" ]; then
    mkdir $LOG_PATH
fi

echo "## outputs of the diff tool" >> $LOG
python diff.py $CONFIG $IOFILE >> $LOG
