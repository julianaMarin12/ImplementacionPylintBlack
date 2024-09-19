# Use the official Python 3.12 image as the base image
FROM python:3.12

# Copy the application code from the host machine's ./app directory to the /app directory in the container
COPY ./app /app

# Copy the requirements.txt file from the host machine to the /app directory in the container
COPY ./requirements.txt /app

# Set the working directory inside the container to /app
WORKDIR /app

# Update and upgrade the package list, install the MariaDB client, and install the MySQL client library for Python
RUN apt-get update && apt-get upgrade -y && apt-get install -y mariadb-client && pip install mysqlclient

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install all the dependencies listed in the requirements.txt file
RUN pip install -r requirements.txt

# Set the command to run the Uvicorn server when the container starts, 
# binding to all interfaces (0.0.0.0) on port 8000 and using the "main" module and "app" object as the entry point
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
