FROM python:latest

RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY GRPC-SNAKE/ /service/GRPC-SNAKE/
WORKDIR /service/GRPC-SNAKE
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/protobuffer.proto

EXPOSE 50051
ENTRYPOINT [ "python", "server.py" ]
