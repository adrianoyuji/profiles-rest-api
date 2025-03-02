# Use official Python image as base
FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port Django runs on
EXPOSE 8000

# Start the Django server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "your_project.wsgi:application"]