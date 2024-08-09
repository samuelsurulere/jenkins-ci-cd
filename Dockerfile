# Base image
FROM python:3.11-slim-buster

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Updating the package list
RUN pip3 install --upgrade pip

# Copying all the files to the source directory
COPY . /code

# Set permissions for the code directory
RUN chmod +x /code/src

# Installing the dependencies
RUN pip3 install --no-cache-dir --upgrade -r code/src/requirements.txt

# Exposing the port that Streamlit runs on
EXPOSE 8080

# Setting the working directory
WORKDIR /code/src

# Giving Python access to all the executable files by adding them to the PATH
ENV PYTHONPATH "${PYTHONPATH}:/code/src"

# Run the Streamlit app
CMD pip3 install -e .