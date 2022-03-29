#Setting base img as python as it used
FROM python:3.8
#Key value pair for docker img
LABEL maintainer="Katie Gamanji"
#copy files from host to container filesystem
COPY . /app
#defining work directory 
WORKDIR /app
RUN pip install -r requirements.txt

# command to run on container start
CMD [ "python", "app.py" ]
