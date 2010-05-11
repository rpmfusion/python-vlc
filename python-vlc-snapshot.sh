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
git clone git://git.videolan.org/vlc/bindings/python.git
version=$(cat python/setup.py |grep version|sed -e "s|.*= '||" -e "s|',||")
mv python $name-$version
rm -fr $name-$version/.git
file=$name-$version-"$sdate"git.tar.bz2
tar jcvf "$pwd"/$file $name-$version/
echo "Wrote: " $file
popd > /dev/null
