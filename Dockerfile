# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the Django project code to the container
COPY . .

# Install Nginx
RUN apt-get update && apt-get install -y nginx

# Remove the default Nginx configuration
RUN rm /etc/nginx/sites-enabled/default

# Copy your custom Nginx configuration file
COPY nginx.conf /etc/nginx/conf.d/

# Expose the port on which your Django app will run (usually 7903)
EXPOSE 7903

# Start Nginx and run your Django app
CMD service nginx start && python manage.py runserver 0.0.0.0:7903