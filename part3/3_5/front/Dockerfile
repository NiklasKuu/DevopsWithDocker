FROM node:alpine
ENV REACT_APP_BACKEND_URL=http://localhost:8080
WORKDIR /app/frontend
COPY ./example-frontend .
RUN npm install && npm install -g serve && npm run build && \
    chmod a+x /app/frontend && adduser -D appuser 
USER appuser
EXPOSE 5000
ENTRYPOINT serve -s -l 5000 build