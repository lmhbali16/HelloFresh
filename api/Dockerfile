FROM python:3.9

WORKDIR /api

RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean
# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
COPY . /api