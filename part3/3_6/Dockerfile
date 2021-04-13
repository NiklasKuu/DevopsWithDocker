FROM node:alpine as build-stage
WORKDIR /app/frontend
COPY ./example-frontend .
RUN npm install && npm run build

FROM node:alpine
WORKDIR /app/frontend
COPY --from=build-stage /app/frontend/build /app/frontend/build
ENV REACT_APP_BACKEND_URL=http://localhost:8080
RUN npm install -g serve && \
    chmod a+x /app/frontend && adduser -D appuser 
USER appuser
EXPOSE 5000
ENTRYPOINT serve -s -l 5000 build