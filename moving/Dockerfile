FROM python:3.9.1

MAINTAINER Backend Developer DONG

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /usr/src/MarketDesign_Project/moving/

WORKDIR /usr/src/MarketDesign_Project/moving

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/MarketDesign_Project/moving
EXPOSE 8000