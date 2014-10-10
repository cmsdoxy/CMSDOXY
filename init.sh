#!/bin/bash

REPOBASE=`pwd`
export DATA=$REPOBASE/data/
export TMP=$REPOBASE/tmp/
if [ ! -d "$TMP" ]; then
    mkdir $TMP
fi
export PYTHONPATH="$PYTHONPATH:$REPOBASE"
