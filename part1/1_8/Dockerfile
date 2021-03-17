FROM ubuntu:18.04

COPY script.sh .
RUN apt-get update && apt-get install -y curl
CMD ["bash", "./script.sh" ]
