FROM ubuntu:18.04
RUN apt-get update -qy
RUN apt-get install -qy python3 python3-pip python3-dev
RUN apt-get update && apt-get clean
COPY . /home
WORKDIR /home
RUN pip3 install -r requirements.txt