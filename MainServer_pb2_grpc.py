# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from SSM.server.grpcproto import MainServer_pb2 as SSM_dot_server_dot_grpcproto_dot_MainServer__pb2


class MainServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendMessage = channel.unary_unary(
                '/MainServer/SendMessage',
                request_serializer=SSM_dot_server_dot_grpcproto_dot_MainServer__pb2.Message.SerializeToString,
                response_deserializer=SSM_dot_server_dot_grpcproto_dot_MainServer__pb2.MessageResponse.FromString,
                )
        self.CreateAccount = channel.unary_unary(
                '/MainServer/CreateAccount',
                request_serializer=SSM_dot_server_dot_grpcproto_dot_MainServer__pb2.CreateAccountData.SerializeToString,
                response_deserializer=SSM_dot_server_dot_grpcproto_dot_MainServer__pb2.AccountDataResponse.FromString,
                )
        self.CheckMessage = channel.unary_unary(
                '/MainServer/CheckMessage',
                request_serializer=SSM_dot_server_dot_grpcproto_dot_MainServer__pb2.CheckMessageRequest.SerializeToString,
                response_deserializer=SSM_dot_server_dot_grpcproto_dot_MainServer__pb2.CheckMessageRespons.FromString,
                )


class MainServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MainServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMessage,
                    request_deserializer=SSM_dot_server_dot_grpcproto_dot_MainServer__pb2.Message.FromString,
                    response_serializer=SSM_dot_server_dot_grpcproto_dot_MainServer__pb2.MessageResponse.SerializeToString,
            ),
            'CreateAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateAccount,
                    request_deserializer=SSM_dot_server_dot_grpcproto_dot_MainServer__pb2.CreateAccountData.FromString,
                    response_serializer=SSM_dot_server_dot_grpcproto_dot_MainServer__pb2.AccountDataResponse.SerializeToString,
            ),
            'CheckMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckMessage,
                    request_deserializer=SSM_dot_server_dot_grpcproto_dot_MainServer__pb2.CheckMessageRequest.FromString,
                    response_serializer=SSM_dot_server_dot_grpcproto_dot_MainServer__pb2.CheckMessageRespons.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MainServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MainServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MainServer/SendMessage',
            SSM_dot_server_dot_grpcproto_dot_MainServer__pb2.Message.SerializeToString,
            SSM_dot_server_dot_grpcproto_dot_MainServer__pb2.MessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MainServer/CreateAccount',
            SSM_dot_server_dot_grpcproto_dot_MainServer__pb2.CreateAccountData.SerializeToString,
            SSM_dot_server_dot_grpcproto_dot_MainServer__pb2.AccountDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MainServer/CheckMessage',
            SSM_dot_server_dot_grpcproto_dot_MainServer__pb2.CheckMessageRequest.SerializeToString,
            SSM_dot_server_dot_grpcproto_dot_MainServer__pb2.CheckMessageRespons.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
