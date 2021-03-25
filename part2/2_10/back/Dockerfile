FROM ubuntu

RUN apt-get update
RUN apt-get install git -y
RUN apt-get install curl -y
WORKDIR /usr/local
RUN curl https://dl.google.com/go/go1.16.2.linux-amd64.tar.gz --output go1.16.2.linux-amd64.tar.gz
RUN rm -rf /usr/local/go && tar -C /usr/local -xzf go1.16.2.linux-amd64.tar.gz
ENV PATH=$PATH:/usr/local/go/bin
WORKDIR /app
RUN git clone https://github.com/docker-hy/material-applications.git
WORKDIR /app/material-applications/example-backend/
ENV REQUEST_ORIGIN=http://localhost:5000
RUN go build
EXPOSE 8080
ENTRYPOINT ./server