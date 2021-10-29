# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import recommendations_pb2 as recommendations__pb2


class RecommendationsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Recommend = channel.unary_unary(
                '/Recommendations/Recommend',
                request_serializer=recommendations__pb2.RecommendationRequest.SerializeToString,
                response_deserializer=recommendations__pb2.RecommendationRespose.FromString,
                )


class RecommendationsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Recommend(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RecommendationsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Recommend': grpc.unary_unary_rpc_method_handler(
                    servicer.Recommend,
                    request_deserializer=recommendations__pb2.RecommendationRequest.FromString,
                    response_serializer=recommendations__pb2.RecommendationRespose.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Recommendations', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Recommendations(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Recommend(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Recommendations/Recommend',
            recommendations__pb2.RecommendationRequest.SerializeToString,
            recommendations__pb2.RecommendationRespose.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
