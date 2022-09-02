FROM python:3.8

WORKDIR /python-learning

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

