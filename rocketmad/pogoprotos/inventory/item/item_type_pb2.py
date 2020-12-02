# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/inventory/item/item_type.proto

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
  name='pogoprotos/inventory/item/item_type.proto',
  package='pogoprotos.inventory.item',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n)pogoprotos/inventory/item/item_type.proto\x12\x19pogoprotos.inventory.item*\x81\x05\n\x08ItemType\x12\x12\n\x0eITEM_TYPE_NONE\x10\x00\x12\x16\n\x12ITEM_TYPE_POKEBALL\x10\x01\x12\x14\n\x10ITEM_TYPE_POTION\x10\x02\x12\x14\n\x10ITEM_TYPE_REVIVE\x10\x03\x12\x11\n\rITEM_TYPE_MAP\x10\x04\x12\x14\n\x10ITEM_TYPE_BATTLE\x10\x05\x12\x12\n\x0eITEM_TYPE_FOOD\x10\x06\x12\x14\n\x10ITEM_TYPE_CAMERA\x10\x07\x12\x12\n\x0eITEM_TYPE_DISK\x10\x08\x12\x17\n\x13ITEM_TYPE_INCUBATOR\x10\t\x12\x15\n\x11ITEM_TYPE_INCENSE\x10\n\x12\x16\n\x12ITEM_TYPE_XP_BOOST\x10\x0b\x12\x1f\n\x1bITEM_TYPE_INVENTORY_UPGRADE\x10\x0c\x12#\n\x1fITEM_TYPE_EVOLUTION_REQUIREMENT\x10\r\x12\x19\n\x15ITEM_TYPE_MOVE_REROLL\x10\x0e\x12\x13\n\x0fITEM_TYPE_CANDY\x10\x0f\x12\x19\n\x15ITEM_TYPE_RAID_TICKET\x10\x10\x12\x1c\n\x18ITEM_TYPE_STARDUST_BOOST\x10\x11\x12\x1d\n\x19ITEM_TYPE_FRIEND_GIFT_BOX\x10\x12\x12\x19\n\x15ITEM_TYPE_TEAM_CHANGE\x10\x13\x12\"\n\x1eITEM_TYPE_VS_SEEKER_BATTLE_NOW\x10\x15\x12\x1d\n\x19ITEM_TYPE_INCIDENT_TICKET\x10\x16\x12!\n\x1dITEM_TYPE_GLOBAL_EVENT_TICKET\x10\x17\x12\x1f\n\x1bITEM_TYPE_STICKER_INVENTORY\x10\x18\x62\x06proto3')
)

_ITEMTYPE = _descriptor.EnumDescriptor(
  name='ItemType',
  full_name='pogoprotos.inventory.item.ItemType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_POKEBALL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_POTION', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_REVIVE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_MAP', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_BATTLE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_FOOD', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_CAMERA', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_DISK', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_INCUBATOR', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_INCENSE', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_XP_BOOST', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_INVENTORY_UPGRADE', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_EVOLUTION_REQUIREMENT', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_MOVE_REROLL', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_CANDY', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_RAID_TICKET', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_STARDUST_BOOST', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_FRIEND_GIFT_BOX', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_TEAM_CHANGE', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_VS_SEEKER_BATTLE_NOW', index=20, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_INCIDENT_TICKET', index=21, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_GLOBAL_EVENT_TICKET', index=22, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_STICKER_INVENTORY', index=23, number=24,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=73,
  serialized_end=714,
)
_sym_db.RegisterEnumDescriptor(_ITEMTYPE)

ItemType = enum_type_wrapper.EnumTypeWrapper(_ITEMTYPE)
ITEM_TYPE_NONE = 0
ITEM_TYPE_POKEBALL = 1
ITEM_TYPE_POTION = 2
ITEM_TYPE_REVIVE = 3
ITEM_TYPE_MAP = 4
ITEM_TYPE_BATTLE = 5
ITEM_TYPE_FOOD = 6
ITEM_TYPE_CAMERA = 7
ITEM_TYPE_DISK = 8
ITEM_TYPE_INCUBATOR = 9
ITEM_TYPE_INCENSE = 10
ITEM_TYPE_XP_BOOST = 11
ITEM_TYPE_INVENTORY_UPGRADE = 12
ITEM_TYPE_EVOLUTION_REQUIREMENT = 13
ITEM_TYPE_MOVE_REROLL = 14
ITEM_TYPE_CANDY = 15
ITEM_TYPE_RAID_TICKET = 16
ITEM_TYPE_STARDUST_BOOST = 17
ITEM_TYPE_FRIEND_GIFT_BOX = 18
ITEM_TYPE_TEAM_CHANGE = 19
ITEM_TYPE_VS_SEEKER_BATTLE_NOW = 21
ITEM_TYPE_INCIDENT_TICKET = 22
ITEM_TYPE_GLOBAL_EVENT_TICKET = 23
ITEM_TYPE_STICKER_INVENTORY = 24


DESCRIPTOR.enum_types_by_name['ItemType'] = _ITEMTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)