FROM python:3.12
RUN curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | sh

RUN apt-get update -y && \
    apt-get install -y azure-cli

RUN apt-get update -y && \
    apt-get install -y git

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the requirements.txt 
COPY requirements.txt requirements.txt


# Install dependencies from the requirements.txt in venv
RUN uv venv --python '>=3.11' default_python_venv && . /default_python_venv/bin/activate && uv pip install -r requirements.txt


WORKDIR /project

COPY ./ .

# Add alias for 'unicon' globally
RUN echo 'unicon() { python3 "$(find /workspaces -maxdepth 4 -type f -name cli.py 2>/dev/null)"; }' >> /etc/bash.bashrc
