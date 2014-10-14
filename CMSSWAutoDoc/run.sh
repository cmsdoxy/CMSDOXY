#!/bin/bash

BASE=`pwd`
cd ../
source init.sh
cd $BASE

python diff.py
