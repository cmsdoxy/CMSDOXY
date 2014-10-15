#!/bin/bash

WORK_DIR=$(pwd)
BASE=$(dirname $(readlink -f "${BASH_SOURCE[0]}"))
cd $BASE
source init.sh

rm -rf $TMP $LOGS

cd $WORK_DIR
