# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/social/social_request.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.networking.requests.social import social_action_pb2 as pogoprotos_dot_networking_dot_requests_dot_social_dot_social__action__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/social/social_request.proto',
  package='pogoprotos.networking.requests.social',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n:pogoprotos/networking/requests/social/social_request.proto\x12%pogoprotos.networking.requests.social\x1a\x39pogoprotos/networking/requests/social/social_action.proto\"t\n\rSocialRequest\x12J\n\rsocial_action\x18\x01 \x01(\x0e\x32\x33.pogoprotos.networking.requests.social.SocialAction\x12\x17\n\x0frequest_message\x18\x02 \x01(\x0c\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_networking_dot_requests_dot_social_dot_social__action__pb2.DESCRIPTOR,])




_SOCIALREQUEST = _descriptor.Descriptor(
  name='SocialRequest',
  full_name='pogoprotos.networking.requests.social.SocialRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='social_action', full_name='pogoprotos.networking.requests.social.SocialRequest.social_action', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_message', full_name='pogoprotos.networking.requests.social.SocialRequest.request_message', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=160,
  serialized_end=276,
)

_SOCIALREQUEST.fields_by_name['social_action'].enum_type = pogoprotos_dot_networking_dot_requests_dot_social_dot_social__action__pb2._SOCIALACTION
DESCRIPTOR.message_types_by_name['SocialRequest'] = _SOCIALREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SocialRequest = _reflection.GeneratedProtocolMessageType('SocialRequest', (_message.Message,), dict(
  DESCRIPTOR = _SOCIALREQUEST,
  __module__ = 'pogoprotos.networking.requests.social.social_request_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.social.SocialRequest)
  ))
_sym_db.RegisterMessage(SocialRequest)


# @@protoc_insertion_point(module_scope)