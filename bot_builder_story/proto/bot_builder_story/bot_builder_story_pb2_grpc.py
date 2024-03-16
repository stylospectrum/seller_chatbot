# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import bot_builder_story_pb2 as bot__builder__story__pb2


class BotBuilderStoryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetStoryBlocks = channel.unary_unary(
            "/bot_builder_story.service.BotBuilderStoryService/GetStoryBlocks",
            request_serializer=bot__builder__story__pb2.GetStoryBlocksRequest.SerializeToString,
            response_deserializer=bot__builder__story__pb2.StoryBlock.FromString,
        )
        self.GetBotResponses = channel.unary_unary(
            "/bot_builder_story.service.BotBuilderStoryService/GetBotResponses",
            request_serializer=bot__builder__story__pb2.GetBotResponsesRequest.SerializeToString,
            response_deserializer=bot__builder__story__pb2.GetBotResponsesResponse.FromString,
        )


class BotBuilderStoryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetStoryBlocks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetBotResponses(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_BotBuilderStoryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetStoryBlocks": grpc.unary_unary_rpc_method_handler(
            servicer.GetStoryBlocks,
            request_deserializer=bot__builder__story__pb2.GetStoryBlocksRequest.FromString,
            response_serializer=bot__builder__story__pb2.StoryBlock.SerializeToString,
        ),
        "GetBotResponses": grpc.unary_unary_rpc_method_handler(
            servicer.GetBotResponses,
            request_deserializer=bot__builder__story__pb2.GetBotResponsesRequest.FromString,
            response_serializer=bot__builder__story__pb2.GetBotResponsesResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "bot_builder_story.service.BotBuilderStoryService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class BotBuilderStoryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetStoryBlocks(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/bot_builder_story.service.BotBuilderStoryService/GetStoryBlocks",
            bot__builder__story__pb2.GetStoryBlocksRequest.SerializeToString,
            bot__builder__story__pb2.StoryBlock.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetBotResponses(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/bot_builder_story.service.BotBuilderStoryService/GetBotResponses",
            bot__builder__story__pb2.GetBotResponsesRequest.SerializeToString,
            bot__builder__story__pb2.GetBotResponsesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
