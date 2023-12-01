#Use the official Python image
FROM python:3.8-slim

#Set the working directory
WORKDIR /src

#Copy the requirements file into the container
COPY src/requirements.txt .

#Install dependencies
RUN  pip install pipenv --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
ADD . .

#Expose the port that Flask will run on
EXPOSE 5000

#Run tests using pytest
CMD [ "pytest"]