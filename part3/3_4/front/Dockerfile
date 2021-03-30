FROM ubuntu
ENV REACT_APP_BACKEND_URL=http://localhost:8080

RUN apt-get update && \
    apt-get install git -y && \
    apt-get install curl -y && \
    curl -sL https://deb.nodesource.com/setup_14.x | bash && \
    apt-get install -y nodejs && \
    mkdir /app && \
    cd /app && \
    git clone https://github.com/docker-hy/material-applications.git && \
    cd /app/material-applications/example-frontend/ && \
    npm install && \
    npm install -g serve && \
    cp -R /app/material-applications/example-frontend/ /app/frontend/ && \
    rm -rf /app/material-applications && \
    chmod a+x /app/frontend/ && \
    cd /app/frontend && \
    npm run build && \
    apt-get purge -y --auto-remove curl && \ 
    rm -rf /var/lib/apt/lists/* && \
    apt-get purge -y --auto-remove git && \
    useradd -m appuser

USER appuser
EXPOSE 5000
ENTRYPOINT serve -s -l 5000 build