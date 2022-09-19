# Creating our Docker file to create an image of our application

# init a base image (We are choosing alpine since it's small Linux distro)
FROM python:3.10-alpine

# define the present working directory
WORKDIR /energie_project_with_api

# copy the content into the working directory dir
ADD . .

# Run pip to install the dependencies of the flask application
RUN pip install -r requirements.txt

# define the command to start the container
CMD ["python", "Project/server.py"]