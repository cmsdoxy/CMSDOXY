#!/bin/bash

WORK_DIR=$(pwd)
BASE=$(dirname $(readlink -f "${BASH_SOURCE[0]}"))
cd $BASE
source init.sh

# Redirect stdout ( > ) into a named pipe ( >() ) running "tee"
exec > >(tee -a "${LOG_PATH}/${LOG_DATE}.log")
# capture stderr
exec 2>&1

echo "## outputs of the diff tool"
python diff.py $CONFIG $IOFILE

EXIT_CODE=$(echo $?)
if [ "$EXIT_CODE" -ne 0 ]; then
    echo "ERROR: diff tool didn't return zero."
    exit 1
fi

cd $WORK_DIR

echo "## $IOFILE has been created."
echo ""
