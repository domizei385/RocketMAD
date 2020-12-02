# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/input_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/input_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n(pogoprotos/settings/input_settings.proto\x12\x13pogoprotos.settings\"\x80\x01\n\rInputSettings\x12%\n\x1d\x65nable_frame_independent_spin\x18\x01 \x01(\x08\x12)\n!milliseconds_processed_spin_force\x18\x02 \x01(\x05\x12\x1d\n\x15spin_speed_multiplier\x18\x03 \x01(\x02\x62\x06proto3')
)




_INPUTSETTINGS = _descriptor.Descriptor(
  name='InputSettings',
  full_name='pogoprotos.settings.InputSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enable_frame_independent_spin', full_name='pogoprotos.settings.InputSettings.enable_frame_independent_spin', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='milliseconds_processed_spin_force', full_name='pogoprotos.settings.InputSettings.milliseconds_processed_spin_force', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spin_speed_multiplier', full_name='pogoprotos.settings.InputSettings.spin_speed_multiplier', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=66,
  serialized_end=194,
)

DESCRIPTOR.message_types_by_name['InputSettings'] = _INPUTSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InputSettings = _reflection.GeneratedProtocolMessageType('InputSettings', (_message.Message,), dict(
  DESCRIPTOR = _INPUTSETTINGS,
  __module__ = 'pogoprotos.settings.input_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.InputSettings)
  ))
_sym_db.RegisterMessage(InputSettings)


# @@protoc_insertion_point(module_scope)