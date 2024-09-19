# Use the official MySQL 8.0 image as the base image
FROM mysql:8.0

# Set environment variables for MySQL configuration
# MYSQL_ROOT_PASSWORD: Defines the password for the root user
ENV MYSQL_ROOT_PASSWORD root

# MYSQL_DATABASE: Defines the name of the default database to be created when the container starts
ENV MYSQL_DATABASE practica_contenedores

# MYSQL_USER: Defines a custom MySQL user to be created in the container
ENV MYSQL_USER eam-user

# MYSQL_PASSWORD: Defines the password for the custom user created with MYSQL_USER
ENV MYSQL_PASSWORD root

# Expose port 3306 to allow connections to MySQL from outside the container
EXPOSE 3306
