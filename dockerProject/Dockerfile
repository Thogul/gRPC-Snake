FROM python:latest
ENV TZ=Europe/Oslo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime  && echo $TZ > /etc/timezone
RUN apt-get --fix-missing -y update
RUN apt-get install -y python3

RUN mkdir /build
ADD ../server.py /build/ 

WORKDIR /build/
RUN python3 -m pip install -r ./gRPC-Snake./requirements.txt
ENTRYPOINT ["server"]
#Dockerfile
