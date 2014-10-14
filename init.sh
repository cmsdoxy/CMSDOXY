#!/bin/bash

REPOBASE=$(dirname $(readlink -f "${BASH_SOURCE[0]}"))
export DATA=$REPOBASE/data/
export LOGS=$REPOBASE/logs
export TMP=$REPOBASE/tmp/
if [ ! -d "$TMP" ]; then
    mkdir $TMP
fi

if [ ! -d "$LOGS" ]; then
    mkdir $LOGS
fi

export PYTHONPATH="$PYTHONPATH:$REPOBASE"
