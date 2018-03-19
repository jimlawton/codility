#!/bin/bash

if [ -z "$1" -o -z "$2" ]; then
    echo "usage: $0 <section> <challenge_name>" 1>&2
    exit 1
fi

newdir="lessons/$1/$2"
if [ -d "$newdir" ]; then
    echo "Directory $newdir already exists!" 1>&2
    exit 1
fi

mkdir -p "$newdir"
if [ $? -ne 0 ]; then
    echo "ERROR: failed to create challenge directory $newdir!"
    exit 1
fi

cd "$newdir"
cp -R ../../00/0_template/ . 
if [ $? -ne 0 ]; then
    echo "ERROR: failed to add challenge!"
    exit 1
fi

