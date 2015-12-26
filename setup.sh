#!/bin/bash

if [ ! -n $1 ]; then
    $1=""
fi

[ ! -n "$(command -v pip)" ] && echo "Requires pip to install" && exit
[ ! -n "$(command -v npm)" ] && echo "Requires npm to install" && exit
[ ! -n "$(command -v bower)" ] && echo "Missing bower. Installing it" && sudo npm install -g bower

# python
pip install -r requirements/common.txt

# bower - frontend
python manage.py bower install $1

# npm - precompilers
(cd components ; npm install)

# django
python manage.py migrate $1
