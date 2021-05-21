FROM python:latest

COPY . /server
WORKDIR /server

RUN pip install -r ./requirements.txt

EXPOSE 50051

ENTRYPOINT [ "python", "server.py" , "True"]
