FROM python:3.12

RUN apt-get update -y && \
    apt-get install -y azure-cli

RUN apt-get update -y && \
apt-get install -y git

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY requirements.txt requirements.txt

RUN uv pip install --no-cache --system -r requirements.txt 

WORKDIR /project

COPY ./ /project