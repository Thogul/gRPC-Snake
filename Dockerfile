FROM python:latest

COPY . /server
WORKDIR /server

RUN pip install -r ./requirements.txt

ENTRYPOINT [ "python", "server.py" , "True"]
