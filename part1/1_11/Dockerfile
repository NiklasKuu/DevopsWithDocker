FROM openjdk:8
WORKDIR /java_button
COPY . .
RUN ./mvnw package
EXPOSE 8080
ENTRYPOINT java -jar ./target/docker-example-1.1.3.jar
