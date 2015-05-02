#!/bin/bash

# python
pip install -r requirements/common.txt

# bower - frontent
python manage.py bower install

# npm - precompilers
cd components
npm install
cd ..

# django
python manage.py migrate
