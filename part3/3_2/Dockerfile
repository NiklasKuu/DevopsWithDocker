FROM ubuntu

RUN apt-get update
RUN apt-get install git -y
RUN apt-get install curl -y
RUN apt-get install docker.io -y
RUN apt install python3 -y


WORKDIR /app/repodownloader
COPY . . 
ENTRYPOINT ["python3","main.py"]