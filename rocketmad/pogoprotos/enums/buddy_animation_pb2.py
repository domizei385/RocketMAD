# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/buddy_animation.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/buddy_animation.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n&pogoprotos/enums/buddy_animation.proto\x12\x10pogoprotos.enums*`\n\x0e\x42uddyAnimation\x12\x19\n\x15\x42UDDY_ANIMATION_UNSET\x10\x00\x12\x19\n\x15\x42UDDY_ANIMATION_HAPPY\x10\x01\x12\x18\n\x14\x42UDDY_ANIMATION_HATE\x10\x02\x62\x06proto3')
)

_BUDDYANIMATION = _descriptor.EnumDescriptor(
  name='BuddyAnimation',
  full_name='pogoprotos.enums.BuddyAnimation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BUDDY_ANIMATION_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_ANIMATION_HAPPY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_ANIMATION_HATE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=60,
  serialized_end=156,
)
_sym_db.RegisterEnumDescriptor(_BUDDYANIMATION)

BuddyAnimation = enum_type_wrapper.EnumTypeWrapper(_BUDDYANIMATION)
BUDDY_ANIMATION_UNSET = 0
BUDDY_ANIMATION_HAPPY = 1
BUDDY_ANIMATION_HATE = 2


DESCRIPTOR.enum_types_by_name['BuddyAnimation'] = _BUDDYANIMATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)