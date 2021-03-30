FROM golang:alpine

ENV PATH=$PATH:/usr/local/go/bin
ENV REQUEST_ORIGIN=http://localhost:5000

WORKDIR /app/example-backend
COPY ./example-backend .
RUN go build && \
    chmod a+x /app/example-backend/ && \
    adduser -D appuser 
USER appuser
EXPOSE 8080
ENTRYPOINT ./server