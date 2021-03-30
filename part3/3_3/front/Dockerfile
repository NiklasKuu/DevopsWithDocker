FROM ubuntu

RUN apt-get update
RUN apt-get install git -y
RUN apt-get install curl -y
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash
RUN apt-get install -y nodejs
WORKDIR /app
RUN git clone https://github.com/docker-hy/material-applications.git
WORKDIR /app/material-applications/example-frontend/
RUN npm install
RUN npm install -g serve
ENV REACT_APP_BACKEND_URL=http://localhost:8080

RUN chmod a+x /app/material-applications/example-frontend/
RUN npm run build

RUN useradd -m appuser

USER appuser
EXPOSE 5000
ENTRYPOINT serve -s -l 5000 build