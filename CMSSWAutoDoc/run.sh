#!/bin/bash

BASE=$(dirname $(readlink -f "${BASH_SOURCE[0]}"))
cd $BASE/..
source init.sh
cd $BASE

python diff.py
