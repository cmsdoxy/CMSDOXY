#!/bin/bash

WORK_DIR=$(pwd)
BASE=$(dirname $(readlink -f "${BASH_SOURCE[0]}"))
cd $BASE
source init.sh

echo "## outputs of the diff tool" >> $LOG
python diff.py $CONFIG $IOFILE >> $LOG 2>&1

EXIT_CODE=$(echo $?)
if [ "$EXIT_CODE" -ne 0 ]; then
    echo "ERROR: diff tool didn't return zero." >> $LOG 2>&1
    exit 1
fi

cd $WORK_DIR
