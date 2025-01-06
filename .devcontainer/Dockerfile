FROM python:3.11-slim

# The installer requires curl (and certificates) to download the release archive
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"


ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1
 
# Install the xz-utils package
RUN apt-get update && apt-get install -y xz-utils

#set working directory
WORKDIR /app

#install dependencies
#COPY ./requirements.txt /app
# # RUN pip install --no-cache-dir --upgrade -r requirements.txt

# #copy the scripts to the folder
COPY . /app
RUN uv sync --frozen
