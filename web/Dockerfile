# Use an official Python runtime as the parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# ENV SECRET_KEY mysecretkey
# ENV POSTGRES_USER myuser
# ENV POSTGRES_PASSWORD mypassword
# ENV POSTGRES_DB mydb

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput
RUN ls -la /app/static

# Expose port 8000 (Gunicorn's default port)
EXPOSE 8000

# Start Gunicorn
CMD ["gunicorn", "myapp.wsgi:application", "--bind", "0.0.0.0:8000"]
