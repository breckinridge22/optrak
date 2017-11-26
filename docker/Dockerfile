FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /project
WORKDIR /project
ADD requirements.txt /project/
RUN pip install -r requirements.txt
RUN pip install web3
ADD . /project/optrak
WORKDIR /project/optrak
