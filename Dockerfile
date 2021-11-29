FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /srv
COPY . /srv

RUN pip install -U pip poetry
RUN apt-get update && apt-get install -y --no-install-recommends \
    lpr \
    cups \
    cups-client \
    cups-pdf \
    printer-driver-dymo \
    netcat \
    wget \
    && rm -rf /var/lib/apt/lists/* && \
    cd /srv && \
    tar -xzf dymo-cups-drivers-1.4.0.tar.gz && \
    cp dymo-cups-drivers-1.4.0.5/ppd/* /usr/share/cups/model

RUN poetry install

CMD ["/srv/start.sh"]
