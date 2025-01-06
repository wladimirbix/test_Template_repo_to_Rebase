FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1
 
# Install the xz-utils package
RUN apt-get update && apt-get install -y xz-utils

#set working directory
WORKDIR /app

# #install dependencies
# #COPY ./requirements.txt /app
# # RUN pip install --no-cache-dir --upgrade -r requirements.txt

# #copy the scripts to the folder
# COPY . /app
