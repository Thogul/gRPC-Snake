# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import protobuffer_pb2 as protobuffer__pb2


class GameServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GameStream = channel.unary_stream(
                '/GameServer/GameStream',
                request_serializer=protobuffer__pb2.Action.SerializeToString,
                response_deserializer=protobuffer__pb2.Data.FromString,
                )
        self.GameAction = channel.unary_unary(
                '/GameServer/GameAction',
                request_serializer=protobuffer__pb2.Action.SerializeToString,
                response_deserializer=protobuffer__pb2.Nothing.FromString,
                )
        self.GameScores = channel.unary_unary(
                '/GameServer/GameScores',
                request_serializer=protobuffer__pb2.Nothing.SerializeToString,
                response_deserializer=protobuffer__pb2.HighScores.FromString,
                )


class GameServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GameStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GameAction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GameScores(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GameServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GameStream': grpc.unary_stream_rpc_method_handler(
                    servicer.GameStream,
                    request_deserializer=protobuffer__pb2.Action.FromString,
                    response_serializer=protobuffer__pb2.Data.SerializeToString,
            ),
            'GameAction': grpc.unary_unary_rpc_method_handler(
                    servicer.GameAction,
                    request_deserializer=protobuffer__pb2.Action.FromString,
                    response_serializer=protobuffer__pb2.Nothing.SerializeToString,
            ),
            'GameScores': grpc.unary_unary_rpc_method_handler(
                    servicer.GameScores,
                    request_deserializer=protobuffer__pb2.Nothing.FromString,
                    response_serializer=protobuffer__pb2.HighScores.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'GameServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GameServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GameStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/GameServer/GameStream',
            protobuffer__pb2.Action.SerializeToString,
            protobuffer__pb2.Data.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GameAction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GameServer/GameAction',
            protobuffer__pb2.Action.SerializeToString,
            protobuffer__pb2.Nothing.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GameScores(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GameServer/GameScores',
            protobuffer__pb2.Nothing.SerializeToString,
            protobuffer__pb2.HighScores.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
