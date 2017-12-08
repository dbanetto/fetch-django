FROM python:3.6-stretch
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=settings.docker

# Install nodejs and npm (LTS v8)
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && apt install -y nodejs

# install bower
RUN npm install -g bower
RUN echo '{ "allow_root": true }' > /root/.bowerrc

# make directories
RUN mkdir /code
RUN mkdir /components

# install requirements
ADD requirements/ /requirements
RUN pip install --upgrade pip
RUN pip install -r /requirements/production.txt
RUN pip install -r /requirements/common.txt

WORKDIR /code

# setup folder
ADD . /code/

RUN python3 manage.py bower install
