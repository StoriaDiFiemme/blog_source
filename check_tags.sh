#!/bin/bash

if [[ -n $1 ]]
then
    grep tags scheduled/documento-del-mese-202* content/documento-del-mese-20* | grep -E "$@"
else
    grep -h tags scheduled/documento-del-mese-202* content/documento-del-mese-20* | sed -r -e s,".*tags:",, -e s/", "/,/g | tr "," \\n | sort | uniq -c
fi
