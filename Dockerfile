#Use the official Python image
FROM python:3.8-slim

# Copy the current directory contents into the container at /app
ADD . /app/

#Set the working directory
WORKDIR /app

#Install dependencies
RUN  pip install pipenv --no-cache-dir -r requirements.txt


#Expose the port that Flask will run on
EXPOSE 5000
