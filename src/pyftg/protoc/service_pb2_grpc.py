"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import service_pb2 as service__pb2

class ServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RunGame = channel.unary_unary('/service.Service/RunGame', request_serializer=service__pb2.RunGameRequest.SerializeToString, response_deserializer=service__pb2.RunGameResponse.FromString)
        self.Spectate = channel.unary_stream('/service.Service/Spectate', request_serializer=service__pb2.SpectateRequest.SerializeToString, response_deserializer=service__pb2.SpectatorGameState.FromString)
        self.Initialize = channel.unary_unary('/service.Service/Initialize', request_serializer=service__pb2.InitializeRequest.SerializeToString, response_deserializer=service__pb2.InitializeResponse.FromString)
        self.Participate = channel.unary_stream('/service.Service/Participate', request_serializer=service__pb2.ParticipateRequest.SerializeToString, response_deserializer=service__pb2.PlayerGameState.FromString)
        self.Input = channel.unary_unary('/service.Service/Input', request_serializer=service__pb2.PlayerInput.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString)

class ServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RunGame(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Spectate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Initialize(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Participate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Input(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_ServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'RunGame': grpc.unary_unary_rpc_method_handler(servicer.RunGame, request_deserializer=service__pb2.RunGameRequest.FromString, response_serializer=service__pb2.RunGameResponse.SerializeToString), 'Spectate': grpc.unary_stream_rpc_method_handler(servicer.Spectate, request_deserializer=service__pb2.SpectateRequest.FromString, response_serializer=service__pb2.SpectatorGameState.SerializeToString), 'Initialize': grpc.unary_unary_rpc_method_handler(servicer.Initialize, request_deserializer=service__pb2.InitializeRequest.FromString, response_serializer=service__pb2.InitializeResponse.SerializeToString), 'Participate': grpc.unary_stream_rpc_method_handler(servicer.Participate, request_deserializer=service__pb2.ParticipateRequest.FromString, response_serializer=service__pb2.PlayerGameState.SerializeToString), 'Input': grpc.unary_unary_rpc_method_handler(servicer.Input, request_deserializer=service__pb2.PlayerInput.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('service.Service', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Service(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RunGame(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/service.Service/RunGame', service__pb2.RunGameRequest.SerializeToString, service__pb2.RunGameResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Spectate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_stream(request, target, '/service.Service/Spectate', service__pb2.SpectateRequest.SerializeToString, service__pb2.SpectatorGameState.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Initialize(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/service.Service/Initialize', service__pb2.InitializeRequest.SerializeToString, service__pb2.InitializeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Participate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_stream(request, target, '/service.Service/Participate', service__pb2.ParticipateRequest.SerializeToString, service__pb2.PlayerGameState.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Input(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/service.Service/Input', service__pb2.PlayerInput.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)