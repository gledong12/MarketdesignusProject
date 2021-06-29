FROM python:3.9.1

MAINTAINER Backend Developer DONG

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /usr/src/MarketDesign_Project/

WORKDIR /usr/src/MarketDesign_Project

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/MarketDesign_Project
EXPOSE 8000