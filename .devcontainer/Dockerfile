FROM python:3.11-slim


#set working directory
WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PATH="/app/.venv/bin:$PATH"

# Install packages
RUN apt-get update && apt-get install -y git
RUN apt-get update && apt-get install -y --no-install-recommends build-essential python3-dev


# # The installer requires curl (and certificates) to download the release archive
# RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# # Download the latest installer
# ADD https://astral.sh/uv/install.sh /uv-installer.sh

# # Run the installer then remove it
# RUN sh /uv-installer.sh && rm /uv-installer.sh

# # Ensure the installed binary is on the `PATH`
# ENV PATH="/root/.local/bin/:$PATH"


ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1
 

#copy the scripts to the folder
COPY . /app



RUN uv sync



#install dependencies
#COPY ./requirements.txt ./
#RUN uv pip install --no-cache-dir --upgrade -r requirements.txt

# #copy the scripts to the folder
#COPY . /app
#RUN uv sync --frozen
