#Use the official Python image
FROM python:3.8-slim

#Set the working directory
WORKDIR /app

#Copy the requirements file into the container
COPY requirements.txt .

#Install dependencies
RUN  pip install pipenv --no-cache-dir -r requirements.txt

#Copy the current directory contents into the container at /app
COPY . /app

#Expose the port that Flask will run on
EXPOSE 5000

#Define the command to run the app
CMD ["python", "app.py"]