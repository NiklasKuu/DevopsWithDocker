FROM ubuntu

ENV PATH=$PATH:/usr/local/go/bin
ENV REQUEST_ORIGIN=http://localhost:5000
RUN apt-get update && \
    apt-get install git -y && \
    apt-get install curl -y && \
    cd /usr/local && \
    curl https://dl.google.com/go/go1.16.2.linux-amd64.tar.gz --output go1.16.2.linux-amd64.tar.gz && \ 
    rm -rf /usr/local/go && tar -C /usr/local -xzf go1.16.2.linux-amd64.tar.gz && \
    mkdir /app && \
    cd /app && \
    git clone https://github.com/docker-hy/material-applications.git && \
    cd /app/material-applications/example-backend/ && \
    go build && \
    cp -R /app/material-applications/example-backend/ /app/backend/ && \
    rm -rf /app/material-applications && \
    chmod a+x /app/backend/ && \
    apt-get purge -y --auto-remove curl && \ 
    rm -rf /var/lib/apt/lists/* && \
    apt-get purge -y --auto-remove git && \
    useradd -m appuser 

USER appuser

EXPOSE 8080
WORKDIR /app/backend/
ENTRYPOINT ./server