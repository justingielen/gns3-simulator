# Use an official Python runtime as a parent image
FROM python:3.9-slim


COPY . /app
RUN make /app
CMD python /app/app.py
