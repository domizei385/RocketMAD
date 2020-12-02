# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/limited_purchase_sku_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/limited_purchase_sku_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n>pogoprotos/settings/master/limited_purchase_sku_settings.proto\x12\x1apogoprotos.settings.master\"\x99\x02\n\x1aLimitedPurchaseSkuSettings\x12\x16\n\x0epurchase_limit\x18\x01 \x01(\x05\x12\x0f\n\x07version\x18\x02 \x01(\x05\x12V\n\x0b\x63hrono_unit\x18\x03 \x01(\x0e\x32\x41.pogoprotos.settings.master.LimitedPurchaseSkuSettings.ChronoUnit\x12\x15\n\rloot_table_id\x18\x04 \x01(\t\x12\x16\n\x0ereset_interval\x18\x14 \x01(\x05\"K\n\nChronoUnit\x12\t\n\x05UNSET\x10\x00\x12\n\n\x06MINUTE\x10\x01\x12\x08\n\x04HOUR\x10\x02\x12\x07\n\x03\x44\x41Y\x10\x03\x12\x08\n\x04WEEK\x10\x04\x12\t\n\x05MONTH\x10\x05\x62\x06proto3')
)



_LIMITEDPURCHASESKUSETTINGS_CHRONOUNIT = _descriptor.EnumDescriptor(
  name='ChronoUnit',
  full_name='pogoprotos.settings.master.LimitedPurchaseSkuSettings.ChronoUnit',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MINUTE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOUR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DAY', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WEEK', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MONTH', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=301,
  serialized_end=376,
)
_sym_db.RegisterEnumDescriptor(_LIMITEDPURCHASESKUSETTINGS_CHRONOUNIT)


_LIMITEDPURCHASESKUSETTINGS = _descriptor.Descriptor(
  name='LimitedPurchaseSkuSettings',
  full_name='pogoprotos.settings.master.LimitedPurchaseSkuSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='purchase_limit', full_name='pogoprotos.settings.master.LimitedPurchaseSkuSettings.purchase_limit', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='pogoprotos.settings.master.LimitedPurchaseSkuSettings.version', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chrono_unit', full_name='pogoprotos.settings.master.LimitedPurchaseSkuSettings.chrono_unit', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loot_table_id', full_name='pogoprotos.settings.master.LimitedPurchaseSkuSettings.loot_table_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reset_interval', full_name='pogoprotos.settings.master.LimitedPurchaseSkuSettings.reset_interval', index=4,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LIMITEDPURCHASESKUSETTINGS_CHRONOUNIT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=376,
)

_LIMITEDPURCHASESKUSETTINGS.fields_by_name['chrono_unit'].enum_type = _LIMITEDPURCHASESKUSETTINGS_CHRONOUNIT
_LIMITEDPURCHASESKUSETTINGS_CHRONOUNIT.containing_type = _LIMITEDPURCHASESKUSETTINGS
DESCRIPTOR.message_types_by_name['LimitedPurchaseSkuSettings'] = _LIMITEDPURCHASESKUSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LimitedPurchaseSkuSettings = _reflection.GeneratedProtocolMessageType('LimitedPurchaseSkuSettings', (_message.Message,), dict(
  DESCRIPTOR = _LIMITEDPURCHASESKUSETTINGS,
  __module__ = 'pogoprotos.settings.master.limited_purchase_sku_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.LimitedPurchaseSkuSettings)
  ))
_sym_db.RegisterMessage(LimitedPurchaseSkuSettings)


# @@protoc_insertion_point(module_scope)