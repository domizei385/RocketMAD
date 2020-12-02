# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/ar_mapping_telemetry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/ar_mapping_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n4pogoprotos/data/telemetry/ar_mapping_telemetry.proto\x12\x19pogoprotos.data.telemetry\"\xaa\t\n\x12\x41rMappingTelemetry\x12_\n\x17\x61r_mapping_telemetry_id\x18\x01 \x01(\x0e\x32>.pogoprotos.data.telemetry.ArMappingTelemetry.ArMappingEventId\x12Q\n\x06source\x18\x02 \x01(\x0e\x32\x41.pogoprotos.data.telemetry.ArMappingTelemetry.ArMappingEntryPoint\x12 \n\x18recording_length_seconds\x18\x03 \x01(\x02\x12\x1c\n\x14time_elapsed_seconds\x18\x04 \x01(\x02\x12\x17\n\x0fpercent_encoded\x18\x05 \x01(\x02\x12\x17\n\x0f\x64\x61ta_size_bytes\x18\x06 \x01(\x03\x12h\n\x19validation_failure_reason\x18\x07 \x01(\x0e\x32\x45.pogoprotos.data.telemetry.ArMappingTelemetry.ValidationFailureReason\"W\n\x17ValidationFailureReason\x12\x12\n\x0eUNKNOWN_REASON\x10\x00\x12\x0c\n\x08TOO_FAST\x10\x01\x12\x0c\n\x08TOO_SLOW\x10\x02\x12\x0c\n\x08TOO_DARK\x10\x03\"\xa7\x01\n\x13\x41rMappingEntryPoint\x12\x11\n\rUNKNOWN_ENTRY\x10\x00\x12\x11\n\rPOI_EDIT_MENU\x10\x01\x12\x12\n\x0ePOI_EDIT_TITLE\x10\x02\x12\x18\n\x14POI_EDIT_DESCRIPTION\x10\x03\x12\x11\n\rPOI_ADD_PHOTO\x10\x04\x12\x15\n\x11POI_EDIT_LOCATION\x10\x05\x12\x12\n\x0ePOI_NOMINATION\x10\x06\"\x80\x04\n\x10\x41rMappingEventId\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0f\n\x0b\x45NTER_STATE\x10\x01\x12\x11\n\rOPT_IN_ACCEPT\x10\x02\x12\x0f\n\x0bOPT_IN_DENY\x10\x03\x12\x13\n\x0fOPT_IN_SETTINGS\x10\x04\x12\x14\n\x10OPT_OUT_SETTINGS\x10\x05\x12\x17\n\x13\x45XIT_FROM_RECORDING\x10\x06\x12\x13\n\x0fSTART_RECORDING\x10\x07\x12\x12\n\x0eSTOP_RECORDING\x10\x08\x12\x13\n\x0f\x43\x41NCEL_ENCODING\x10\t\x12\x0e\n\nUPLOAD_NOW\x10\n\x12\x10\n\x0cUPLOAD_LATER\x10\x0b\x12\x11\n\rCANCEL_UPLOAD\x10\x0c\x12\x19\n\x15START_UPLOAD_SETTINGS\x10\r\x12\x12\n\x0eUPLOAD_SUCCESS\x10\x0e\x12\x15\n\x11OPT_IN_LEARN_MORE\x10\x0f\x12\x15\n\x11\x45XIT_FROM_PREVIEW\x10\x10\x12%\n!SUBMIT_POI_AR_VIDEO_METADATA_FAIL\x10\x11\x12\x12\n\x0eUPLOAD_FAILURE\x10\x12\x12\x1c\n\x18UPLOAD_LATER_WIFI_PROMPT\x10\x13\x12\x0f\n\x0b\x43LEAR_SCANS\x10\x14\x12\x13\n\x0fOPEN_INFO_PANEL\x10\x15\x12\x17\n\x13RESCAN_FROM_PREVIEW\x10\x16\x62\x06proto3')
)



_ARMAPPINGTELEMETRY_VALIDATIONFAILUREREASON = _descriptor.EnumDescriptor(
  name='ValidationFailureReason',
  full_name='pogoprotos.data.telemetry.ArMappingTelemetry.ValidationFailureReason',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_REASON', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOO_FAST', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOO_SLOW', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOO_DARK', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=506,
  serialized_end=593,
)
_sym_db.RegisterEnumDescriptor(_ARMAPPINGTELEMETRY_VALIDATIONFAILUREREASON)

_ARMAPPINGTELEMETRY_ARMAPPINGENTRYPOINT = _descriptor.EnumDescriptor(
  name='ArMappingEntryPoint',
  full_name='pogoprotos.data.telemetry.ArMappingTelemetry.ArMappingEntryPoint',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_ENTRY', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POI_EDIT_MENU', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POI_EDIT_TITLE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POI_EDIT_DESCRIPTION', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POI_ADD_PHOTO', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POI_EDIT_LOCATION', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POI_NOMINATION', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=596,
  serialized_end=763,
)
_sym_db.RegisterEnumDescriptor(_ARMAPPINGTELEMETRY_ARMAPPINGENTRYPOINT)

_ARMAPPINGTELEMETRY_ARMAPPINGEVENTID = _descriptor.EnumDescriptor(
  name='ArMappingEventId',
  full_name='pogoprotos.data.telemetry.ArMappingTelemetry.ArMappingEventId',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENTER_STATE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPT_IN_ACCEPT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPT_IN_DENY', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPT_IN_SETTINGS', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPT_OUT_SETTINGS', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXIT_FROM_RECORDING', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START_RECORDING', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOP_RECORDING', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCEL_ENCODING', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPLOAD_NOW', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPLOAD_LATER', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCEL_UPLOAD', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START_UPLOAD_SETTINGS', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPLOAD_SUCCESS', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPT_IN_LEARN_MORE', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXIT_FROM_PREVIEW', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBMIT_POI_AR_VIDEO_METADATA_FAIL', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPLOAD_FAILURE', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPLOAD_LATER_WIFI_PROMPT', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLEAR_SCANS', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPEN_INFO_PANEL', index=21, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESCAN_FROM_PREVIEW', index=22, number=22,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=766,
  serialized_end=1278,
)
_sym_db.RegisterEnumDescriptor(_ARMAPPINGTELEMETRY_ARMAPPINGEVENTID)


_ARMAPPINGTELEMETRY = _descriptor.Descriptor(
  name='ArMappingTelemetry',
  full_name='pogoprotos.data.telemetry.ArMappingTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ar_mapping_telemetry_id', full_name='pogoprotos.data.telemetry.ArMappingTelemetry.ar_mapping_telemetry_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='pogoprotos.data.telemetry.ArMappingTelemetry.source', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recording_length_seconds', full_name='pogoprotos.data.telemetry.ArMappingTelemetry.recording_length_seconds', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_elapsed_seconds', full_name='pogoprotos.data.telemetry.ArMappingTelemetry.time_elapsed_seconds', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='percent_encoded', full_name='pogoprotos.data.telemetry.ArMappingTelemetry.percent_encoded', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_size_bytes', full_name='pogoprotos.data.telemetry.ArMappingTelemetry.data_size_bytes', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validation_failure_reason', full_name='pogoprotos.data.telemetry.ArMappingTelemetry.validation_failure_reason', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ARMAPPINGTELEMETRY_VALIDATIONFAILUREREASON,
    _ARMAPPINGTELEMETRY_ARMAPPINGENTRYPOINT,
    _ARMAPPINGTELEMETRY_ARMAPPINGEVENTID,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=1278,
)

_ARMAPPINGTELEMETRY.fields_by_name['ar_mapping_telemetry_id'].enum_type = _ARMAPPINGTELEMETRY_ARMAPPINGEVENTID
_ARMAPPINGTELEMETRY.fields_by_name['source'].enum_type = _ARMAPPINGTELEMETRY_ARMAPPINGENTRYPOINT
_ARMAPPINGTELEMETRY.fields_by_name['validation_failure_reason'].enum_type = _ARMAPPINGTELEMETRY_VALIDATIONFAILUREREASON
_ARMAPPINGTELEMETRY_VALIDATIONFAILUREREASON.containing_type = _ARMAPPINGTELEMETRY
_ARMAPPINGTELEMETRY_ARMAPPINGENTRYPOINT.containing_type = _ARMAPPINGTELEMETRY
_ARMAPPINGTELEMETRY_ARMAPPINGEVENTID.containing_type = _ARMAPPINGTELEMETRY
DESCRIPTOR.message_types_by_name['ArMappingTelemetry'] = _ARMAPPINGTELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ArMappingTelemetry = _reflection.GeneratedProtocolMessageType('ArMappingTelemetry', (_message.Message,), dict(
  DESCRIPTOR = _ARMAPPINGTELEMETRY,
  __module__ = 'pogoprotos.data.telemetry.ar_mapping_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.ArMappingTelemetry)
  ))
_sym_db.RegisterMessage(ArMappingTelemetry)


# @@protoc_insertion_point(module_scope)