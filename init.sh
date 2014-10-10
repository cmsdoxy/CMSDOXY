#!/bin/bash

REPOBASE=`pwd`
DATA=$REPOBASE/data
TMP=$REPOBASE/tmp
if [ ! -d "$TMP" ]; then
    mkdir $TMP
fi
export PYTHONPATH="$PYTHONPATH:$REPOBASE"
