#!/bin/bash

set -e

tmp=$(mktemp -d)

trap cleanup EXIT
cleanup() {
    set +e
    [ -z "$tmp" -o ! -d "$tmp" ] || rm -rf "$tmp"
}

unset CDPATH
pwd=$(pwd)
sdate=$(date +%Y%m%d)
name=python-vlc

pushd "$tmp" > /dev/null
# Because git sucks, we download the entire vlc tree:
git clone git://git.videolan.org/vlc.git
pushd vlc > /dev/null
git checkout origin/1.0-bugfix
pushd bindings/python/ > /dev/null
python setup.py sdist
pushd dist > /dev/null
for file in *.tar.gz; do
mv $file "$pwd"/
echo "Wrote: " $file
done
popd > /dev/null
popd > /dev/null
popd > /dev/null
popd > /dev/null
