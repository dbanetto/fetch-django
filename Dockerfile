FROM python:3.6-stretch
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=settings.docker

# Install nodejs and npm (LTS v8)
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
        apt install -y nodejs

# make directories
RUN mkdir /code
WORKDIR /code

# install requirements
ADD requirements/ /requirements
RUN pip install --upgrade pip && \
        pip install -r /requirements/production.txt && \
        pip install -r /requirements/common.txt

# setup folder
ADD . /code/

RUN npm install && \
        python manage.py collectstatic --noinput && \
        echo "Removing node_modules" && \
        rm -rf node_modules

CMD sh /code/bin/docker-entrypoint.sh
