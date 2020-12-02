# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/raid_client_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import raid_level_pb2 as pogoprotos_dot_enums_dot_raid__level__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/raid_client_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n5pogoprotos/settings/master/raid_client_settings.proto\x12\x1apogoprotos.settings.master\x1a!pogoprotos/enums/raid_level.proto\"\xd9\x04\n\x12RaidClientSettings\x12\x1b\n\x13remote_raid_enabled\x18\x01 \x01(\x08\x12\x1e\n\x16max_remote_raid_passes\x18\x02 \x01(\x05\x12\x1e\n\x16remote_damage_modifier\x18\x03 \x01(\x02\x12%\n\x1dremote_raids_min_player_level\x18\x04 \x01(\x05\x12\x1e\n\x16max_num_friend_invites\x18\x05 \x01(\x05\x12%\n\x1d\x66riend_invite_cutoff_time_sec\x18\x06 \x01(\x05\x12$\n\x1c\x63\x61n_invite_friends_in_person\x18\x07 \x01(\x08\x12#\n\x1b\x63\x61n_invite_friends_remotely\x18\x08 \x01(\x08\x12\x1d\n\x15max_players_per_lobby\x18\t \x01(\x05\x12$\n\x1cmax_remote_players_per_lobby\x18\n \x01(\x05\x12\'\n\x1finvite_cooldown_duration_millis\x18\x0b \x01(\x03\x12)\n!max_num_friend_invites_per_action\x18\x0c \x01(\x05\x12O\n*unsupported_raid_levels_for_friend_invites\x18\r \x03(\x0e\x32\x1b.pogoprotos.enums.RaidLevel\x12\x43\n\x1eunsupported_remote_raid_levels\x18\x0e \x03(\x0e\x32\x1b.pogoprotos.enums.RaidLevelb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_raid__level__pb2.DESCRIPTOR,])




_RAIDCLIENTSETTINGS = _descriptor.Descriptor(
  name='RaidClientSettings',
  full_name='pogoprotos.settings.master.RaidClientSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='remote_raid_enabled', full_name='pogoprotos.settings.master.RaidClientSettings.remote_raid_enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_remote_raid_passes', full_name='pogoprotos.settings.master.RaidClientSettings.max_remote_raid_passes', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remote_damage_modifier', full_name='pogoprotos.settings.master.RaidClientSettings.remote_damage_modifier', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remote_raids_min_player_level', full_name='pogoprotos.settings.master.RaidClientSettings.remote_raids_min_player_level', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_num_friend_invites', full_name='pogoprotos.settings.master.RaidClientSettings.max_num_friend_invites', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='friend_invite_cutoff_time_sec', full_name='pogoprotos.settings.master.RaidClientSettings.friend_invite_cutoff_time_sec', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='can_invite_friends_in_person', full_name='pogoprotos.settings.master.RaidClientSettings.can_invite_friends_in_person', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='can_invite_friends_remotely', full_name='pogoprotos.settings.master.RaidClientSettings.can_invite_friends_remotely', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_players_per_lobby', full_name='pogoprotos.settings.master.RaidClientSettings.max_players_per_lobby', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_remote_players_per_lobby', full_name='pogoprotos.settings.master.RaidClientSettings.max_remote_players_per_lobby', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='invite_cooldown_duration_millis', full_name='pogoprotos.settings.master.RaidClientSettings.invite_cooldown_duration_millis', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_num_friend_invites_per_action', full_name='pogoprotos.settings.master.RaidClientSettings.max_num_friend_invites_per_action', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unsupported_raid_levels_for_friend_invites', full_name='pogoprotos.settings.master.RaidClientSettings.unsupported_raid_levels_for_friend_invites', index=12,
      number=13, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unsupported_remote_raid_levels', full_name='pogoprotos.settings.master.RaidClientSettings.unsupported_remote_raid_levels', index=13,
      number=14, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=121,
  serialized_end=722,
)

_RAIDCLIENTSETTINGS.fields_by_name['unsupported_raid_levels_for_friend_invites'].enum_type = pogoprotos_dot_enums_dot_raid__level__pb2._RAIDLEVEL
_RAIDCLIENTSETTINGS.fields_by_name['unsupported_remote_raid_levels'].enum_type = pogoprotos_dot_enums_dot_raid__level__pb2._RAIDLEVEL
DESCRIPTOR.message_types_by_name['RaidClientSettings'] = _RAIDCLIENTSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RaidClientSettings = _reflection.GeneratedProtocolMessageType('RaidClientSettings', (_message.Message,), dict(
  DESCRIPTOR = _RAIDCLIENTSETTINGS,
  __module__ = 'pogoprotos.settings.master.raid_client_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.RaidClientSettings)
  ))
_sym_db.RegisterMessage(RaidClientSettings)


# @@protoc_insertion_point(module_scope)