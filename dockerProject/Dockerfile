FROM python:latest


WORKDIR /gRPC-Snake
COPY gRPC-Snake ./
RUN python -m pip install -r requierments.txt

EXPOSE 50051
ENTRYPOINT [ "python", "server.py" ]
