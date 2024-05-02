#!/bin/bash
# npm install vue-cookies --save

if [ $1 == 'run' ]; then
    npm run serve
else
    rm dist.tar.gz
    npm run build
    tar -zcvf dist.tar.gz dist
fi