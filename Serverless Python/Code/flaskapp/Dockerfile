#CODE1.0:
#use FROM to configure the base container image to build on
#see - https://docs.docker.com/engine/reference/builder/#from

FROM python:3

#CODE1.1:
#use RUN to install the flask python library using the pip command
#see - https://docs.docker.com/engine/reference/builder/#run

RUN pip install flask

#CODE1.2:
#use RUN to create an empty directory to host the python flask main.py application file
#see - https://docs.docker.com/engine/reference/builder/#run

RUN mkdir -p /corp/app

#CODE1.3:
#use WORKDIR to change the current working directory
#see - https://docs.docker.com/engine/reference/builder/#workdir

COPY main.py .

#CODE1.4:
#use COPY to copy across the main.py file into the current working directory
#see - https://docs.docker.com/engine/reference/builder/#copy

ENV FLASK_APP=/corp/app/main.py

#CODE1.5:
#use ENV to set the FLASK_APP environment variable - tells the flask runtime where to start
#see - https://docs.docker.com/engine/reference/builder/#env

ENV FLASK_APP=/corp/app/main.py

#CODE1.6:
#use ENV to set the APP_NAME environment variable - ref and used in the main.py file 
#see - https://docs.docker.com/engine/reference/builder/#env

ENV APP_NAME=CloudAcademy.DevOps.Dockerfile

#CODE1.7:
#use the CMD to set the default execution for the container when launched
#see - https://docs.docker.com/engine/reference/builder/#cmd

CMD ["flask", "run", "--host=0.0.0.0"]
