#!/bin/bash

[ ! -n "$(command -v pip)" ] && echo "Requires pip to install" && exit
[ ! -n "$(command -v npm)" ] && echo "Requires npm to install" && exit
[ ! -n "$(command -v bower)" ] && echo "Requires bower to install" && exit

# python
pip install -r requirements/common.txt

# bower - frontend
python manage.py bower install

# npm - precompilers
(cd components ; npm install)

# django
python manage.py migrate
