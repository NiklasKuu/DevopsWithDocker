FROM golang:alpine AS build-stage

ENV PATH=$PATH:/usr/local/go/bin

WORKDIR /app/example-backend
COPY ./example-backend .
RUN go build -o server

FROM alpine
WORKDIR /app/example-backend
RUN apk update && apk add ca-certificates && \
    rm -f /var/cache/apk/* && \
    chmod a+x /app/example-backend/ && \
    adduser -D appuser 
USER appuser

COPY --from=build-stage /app/example-backend/server /app/example-backend
ENV REQUEST_ORIGIN=http://localhost:5000
EXPOSE 8080
ENTRYPOINT ./server