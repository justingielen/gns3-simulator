# Use an official Python runtime as a parent image
FROM ubuntu:latest


# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Define environment variable
ENV NAME World
RUN pip install numpy

# Run app.py when the container launches
CMD ["python", "app.py"]
