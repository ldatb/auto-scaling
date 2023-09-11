# Author: Lucas de Ataides <lucasatab@gmail.com>

FROM ubuntu:22.04
ARG DEBIAN_FRONTEND=noninteractive
ENV LANG="en_US.UTF-8"
ENV LC_ALL="en_US.UTF-8"
ENV LC_CTYPE="en_US.UTF-8"
USER root

# Update and install dependencies
RUN apt update && apt upgrade -y && apt install --no-install-recommends -y software-properties-common python3-pip

# Clean APT cache to decrease image size
RUN apt clean && rm -rf /var/lib/apt/lists/*

# Create and set user
RUN useradd --create-home autoscale
USER autoscale

# Create and set workdir
RUN mkdir /home/autoscale/app
WORKDIR /home/autoscale/app

# Copy files
COPY /app ./

# Install pipenv
ENV PATH="${HOME}/.local/bin:$PATH"
RUN pip install -U pipenv

# Install dependencies
RUN /home/autoscale/.local/bin/pipenv requirements > requirements.txt
RUN pip install -r requirements.txt

# Make sure all messages always reach console
ENV PYTHONUNBUFFERED=1

# Expose both API port
EXPOSE 5000

# Start the API
CMD [ "python3", "api.py" ]
