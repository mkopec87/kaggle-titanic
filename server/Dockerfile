FROM python:3.8-slim

RUN pip install -U pip

ADD requirements.txt /project/
RUN pip install -r /project/requirements.txt

ADD src /project/src

WORKDIR /project/src/

EXPOSE 5000
