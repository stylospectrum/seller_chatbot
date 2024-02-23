# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bot_builder_nlp.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x62ot_builder_nlp.proto\x12\x17\x62ot_builder_nlp.service\"@\n\tUserInput\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\x16\n\x0estory_block_id\x18\x03 \x01(\t\"b\n\x16UpsertEmbeddingRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x37\n\x0buser_inputs\x18\x02 \x03(\x0b\x32\".bot_builder_nlp.service.UserInput\"*\n\x17UpsertEmbeddingResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"%\n\x16\x44\x65leteEmbeddingRequest\x12\x0b\n\x03ids\x18\x01 \x03(\t\"*\n\x17\x44\x65leteEmbeddingResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"=\n\x16GetStoryBlockIdRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x12\n\nuser_input\x18\x02 \x01(\t\"1\n\x17GetStoryBlockIdResponse\x12\x16\n\x0estory_block_id\x18\x01 \x01(\t2\xf8\x02\n\x14\x42otBuilderNlpService\x12t\n\x0fUpsertEmbedding\x12/.bot_builder_nlp.service.UpsertEmbeddingRequest\x1a\x30.bot_builder_nlp.service.UpsertEmbeddingResponse\x12t\n\x0f\x44\x65leteEmbedding\x12/.bot_builder_nlp.service.DeleteEmbeddingRequest\x1a\x30.bot_builder_nlp.service.DeleteEmbeddingResponse\x12t\n\x0fGetStoryBlockId\x12/.bot_builder_nlp.service.GetStoryBlockIdRequest\x1a\x30.bot_builder_nlp.service.GetStoryBlockIdResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bot_builder_nlp_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_USERINPUT']._serialized_start=50
  _globals['_USERINPUT']._serialized_end=114
  _globals['_UPSERTEMBEDDINGREQUEST']._serialized_start=116
  _globals['_UPSERTEMBEDDINGREQUEST']._serialized_end=214
  _globals['_UPSERTEMBEDDINGRESPONSE']._serialized_start=216
  _globals['_UPSERTEMBEDDINGRESPONSE']._serialized_end=258
  _globals['_DELETEEMBEDDINGREQUEST']._serialized_start=260
  _globals['_DELETEEMBEDDINGREQUEST']._serialized_end=297
  _globals['_DELETEEMBEDDINGRESPONSE']._serialized_start=299
  _globals['_DELETEEMBEDDINGRESPONSE']._serialized_end=341
  _globals['_GETSTORYBLOCKIDREQUEST']._serialized_start=343
  _globals['_GETSTORYBLOCKIDREQUEST']._serialized_end=404
  _globals['_GETSTORYBLOCKIDRESPONSE']._serialized_start=406
  _globals['_GETSTORYBLOCKIDRESPONSE']._serialized_end=455
  _globals['_BOTBUILDERNLPSERVICE']._serialized_start=458
  _globals['_BOTBUILDERNLPSERVICE']._serialized_end=834
# @@protoc_insertion_point(module_scope)
