# Use an official Python runtime as the base image
FROM python:3.9

# Install Nginx
RUN apt-get update && apt-get install -y nginx

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the Nginx configuration file to the container
COPY nginx.conf /etc/nginx/nginx.conf

# Copy the Django project code to the container
COPY . .

# Expose the port on which Nginx will listen (usually 80)
EXPOSE 80

# Start Nginx and your Django app
CMD service nginx start && python manage.py runserver 0.0.0.0:7903