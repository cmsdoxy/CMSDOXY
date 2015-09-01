#!/bin/bash

query="IOError"
currentDir=`pwd`

# go to the path that contain this script
cd $(dirname $(readlink -f "${BASH_SOURCE[0]}"))

source ../init.sh

find $LOGS -name "*.log" | while read logFile; do
    if grep -q $query "$logFile"; then
        echo "$query found in $logFile"
    fi
done

cd $currentDir
