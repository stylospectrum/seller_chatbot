# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bot_builder_story.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x17\x62ot_builder_story.proto\x12\x19\x62ot_builder_story.service"(\n\x15GetStoryBlocksRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t"\x91\x01\n\nStoryBlock\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0f\n\x07user_id\x18\x04 \x01(\t\x12\x11\n\tparent_id\x18\x05 \x01(\t\x12\x37\n\x08\x63hildren\x18\x06 \x03(\x0b\x32%.bot_builder_story.service.StoryBlock"0\n\x16GetBotResponsesRequest\x12\x16\n\x0estory_block_id\x18\x02 \x01(\t"T\n\x17GetBotResponsesResponse\x12\x39\n\tresponses\x18\x01 \x03(\x0b\x32&.bot_builder_story.service.BotResponse"3\n\x11\x42otResponseButton\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\x12\r\n\x05go_to\x18\x02 \x01(\t"\x8c\x01\n\x16\x42otResponseGalleryItem\x12\x0f\n\x07img_url\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12=\n\x07\x62uttons\x18\x04 \x03(\x0b\x32,.bot_builder_story.service.BotResponseButton"\xc1\x01\n\x0b\x42otResponse\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x10\n\x08variants\x18\x02 \x03(\t\x12\x0f\n\x07img_url\x18\x03 \x01(\t\x12=\n\x07\x62uttons\x18\x04 \x03(\x0b\x32,.bot_builder_story.service.BotResponseButton\x12\x42\n\x07gallery\x18\x05 \x03(\x0b\x32\x31.bot_builder_story.service.BotResponseGalleryItem2\xfd\x01\n\x16\x42otBuilderStoryService\x12i\n\x0eGetStoryBlocks\x12\x30.bot_builder_story.service.GetStoryBlocksRequest\x1a%.bot_builder_story.service.StoryBlock\x12x\n\x0fGetBotResponses\x12\x31.bot_builder_story.service.GetBotResponsesRequest\x1a\x32.bot_builder_story.service.GetBotResponsesResponseb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "bot_builder_story_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_GETSTORYBLOCKSREQUEST"]._serialized_start = 54
    _globals["_GETSTORYBLOCKSREQUEST"]._serialized_end = 94
    _globals["_STORYBLOCK"]._serialized_start = 97
    _globals["_STORYBLOCK"]._serialized_end = 242
    _globals["_GETBOTRESPONSESREQUEST"]._serialized_start = 244
    _globals["_GETBOTRESPONSESREQUEST"]._serialized_end = 292
    _globals["_GETBOTRESPONSESRESPONSE"]._serialized_start = 294
    _globals["_GETBOTRESPONSESRESPONSE"]._serialized_end = 378
    _globals["_BOTRESPONSEBUTTON"]._serialized_start = 380
    _globals["_BOTRESPONSEBUTTON"]._serialized_end = 431
    _globals["_BOTRESPONSEGALLERYITEM"]._serialized_start = 434
    _globals["_BOTRESPONSEGALLERYITEM"]._serialized_end = 574
    _globals["_BOTRESPONSE"]._serialized_start = 577
    _globals["_BOTRESPONSE"]._serialized_end = 770
    _globals["_BOTBUILDERSTORYSERVICE"]._serialized_start = 773
    _globals["_BOTBUILDERSTORYSERVICE"]._serialized_end = 1026
# @@protoc_insertion_point(module_scope)
