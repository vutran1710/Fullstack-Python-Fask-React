# pull official base image
FROM python:3.8

# Setup webserver & webapp
RUN apt update
# RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt install lighttpd -y
# - copy lighttpd config to container
COPY webserver/lighttpd.conf /etc/lighttpd

# prepare dir for flask to write files to
# must be the same as set in lighttpd.conf
RUN cd /var && mkdir data && cd ..

# set work directory
WORKDIR /usr/src/flask
COPY ./backend .
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV DATA_DIR=/var/data/

# install dependencies
RUN pip install pipenv
RUN pipenv install --deploy

# Exec
# expose lighttpd port
EXPOSE 3000
# - run lighttpd
# - run backend
CMD service lighttpd start && pipenv run app --bind=0.0.0.0:5000
