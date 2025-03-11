#!/bin/bash
# npm install vue-cookies --save

if [[ $1 == 'run' ]]; then
    npm run serve
elif [[ $1 == 'init' ]]; then
    nvm install 18
    nvm use 18

    npm install -g @vue/cli
    
    npm i
else
    rm dist.tar.gz
    npm run build
    tar -zcvf dist.tar.gz dist
fi