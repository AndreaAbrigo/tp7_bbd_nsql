FROM python:3.7
ADD . /todo
WORKDIR /todo
RUN pip install flask pymongo requests