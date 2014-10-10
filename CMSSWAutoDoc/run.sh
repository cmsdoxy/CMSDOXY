#!/bin/bash

BASE=`pwd`
cd ../
source init.sh
cd $BASE

ls
python diff.py > $TMP/cmsswRels2Doc.txt
