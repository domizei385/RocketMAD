# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/timed_group_challenge_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/timed_group_challenge_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n8pogoprotos/settings/timed_group_challenge_settings.proto\x12\x13pogoprotos.settings\"\xa7\x01\n\x1bTimedGroupChallengeSettings\x12$\n\x1cwidget_auto_update_period_ms\x18\x01 \x01(\x05\x12\x36\n.friend_leaderboard_background_update_period_ms\x18\x02 \x01(\x03\x12*\n\"friend_leaderboard_friends_per_rpc\x18\x03 \x01(\x05\x62\x06proto3')
)




_TIMEDGROUPCHALLENGESETTINGS = _descriptor.Descriptor(
  name='TimedGroupChallengeSettings',
  full_name='pogoprotos.settings.TimedGroupChallengeSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='widget_auto_update_period_ms', full_name='pogoprotos.settings.TimedGroupChallengeSettings.widget_auto_update_period_ms', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='friend_leaderboard_background_update_period_ms', full_name='pogoprotos.settings.TimedGroupChallengeSettings.friend_leaderboard_background_update_period_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='friend_leaderboard_friends_per_rpc', full_name='pogoprotos.settings.TimedGroupChallengeSettings.friend_leaderboard_friends_per_rpc', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=82,
  serialized_end=249,
)

DESCRIPTOR.message_types_by_name['TimedGroupChallengeSettings'] = _TIMEDGROUPCHALLENGESETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TimedGroupChallengeSettings = _reflection.GeneratedProtocolMessageType('TimedGroupChallengeSettings', (_message.Message,), dict(
  DESCRIPTOR = _TIMEDGROUPCHALLENGESETTINGS,
  __module__ = 'pogoprotos.settings.timed_group_challenge_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.TimedGroupChallengeSettings)
  ))
_sym_db.RegisterMessage(TimedGroupChallengeSettings)


# @@protoc_insertion_point(module_scope)