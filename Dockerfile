# sample Dockerfile

FROM python:3.7-alpine

ENV path=newpath:$PATH
ENV APP=myapp

USER root
WORKDIR /workdir

copy requirements.txt .

RUN pip install -r requirements.txt

