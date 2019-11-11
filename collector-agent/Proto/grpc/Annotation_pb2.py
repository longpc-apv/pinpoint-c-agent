# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Annotation.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Annotation.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\n!com.navercorp.pinpoint.grpc.traceB\017AnnotationProtoP\001'),
  serialized_pb=_b('\n\x10\x41nnotation.proto\x1a\x1egoogle/protobuf/wrappers.proto\"V\n\x0fPIntStringValue\x12\x10\n\x08intValue\x18\x01 \x01(\x05\x12\x31\n\x0bstringValue\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\x91\x01\n\x15PIntStringStringValue\x12\x10\n\x08intValue\x18\x01 \x01(\x05\x12\x32\n\x0cstringValue1\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0cstringValue2\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xb4\x01\n\x1ePLongIntIntByteByteStringValue\x12\x11\n\tlongValue\x18\x01 \x01(\x03\x12\x11\n\tintValue1\x18\x02 \x01(\x05\x12\x11\n\tintValue2\x18\x03 \x01(\x05\x12\x12\n\nbyteValue1\x18\x04 \x01(\x11\x12\x12\n\nbyteValue2\x18\x05 \x01(\x11\x12\x31\n\x0bstringValue\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"j\n\x1aPIntBooleanIntBooleanValue\x12\x11\n\tintValue1\x18\x01 \x01(\x05\x12\x12\n\nboolValue1\x18\x02 \x01(\x08\x12\x11\n\tintValue2\x18\x03 \x01(\x05\x12\x12\n\nboolValue2\x18\x04 \x01(\x08\"|\n\x12PStringStringValue\x12\x32\n\x0cstringValue1\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0cstringValue2\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xeb\x03\n\x10PAnnotationValue\x12\x15\n\x0bstringValue\x18\x01 \x01(\tH\x00\x12\x13\n\tboolValue\x18\x02 \x01(\x08H\x00\x12\x12\n\x08intValue\x18\x03 \x01(\x05H\x00\x12\x13\n\tlongValue\x18\x04 \x01(\x03H\x00\x12\x14\n\nshortValue\x18\x05 \x01(\x11H\x00\x12\x15\n\x0b\x64oubleValue\x18\x06 \x01(\x01H\x00\x12\x15\n\x0b\x62inaryValue\x18\x07 \x01(\x0cH\x00\x12\x13\n\tbyteValue\x18\x08 \x01(\x11H\x00\x12*\n\x0eintStringValue\x18\t \x01(\x0b\x32\x10.PIntStringValueH\x00\x12\x30\n\x11stringStringValue\x18\n \x01(\x0b\x32\x13.PStringStringValueH\x00\x12\x36\n\x14intStringStringValue\x18\x0b \x01(\x0b\x32\x16.PIntStringStringValueH\x00\x12H\n\x1dlongIntIntByteByteStringValue\x18\x0c \x01(\x0b\x32\x1f.PLongIntIntByteByteStringValueH\x00\x12@\n\x19intBooleanIntBooleanValue\x18\r \x01(\x0b\x32\x1b.PIntBooleanIntBooleanValueH\x00\x42\x07\n\x05\x66ield\"<\n\x0bPAnnotation\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.PAnnotationValueB6\n!com.navercorp.pinpoint.grpc.traceB\x0f\x41nnotationProtoP\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_PINTSTRINGVALUE = _descriptor.Descriptor(
  name='PIntStringValue',
  full_name='PIntStringValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='intValue', full_name='PIntStringValue.intValue', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stringValue', full_name='PIntStringValue.stringValue', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=52,
  serialized_end=138,
)


_PINTSTRINGSTRINGVALUE = _descriptor.Descriptor(
  name='PIntStringStringValue',
  full_name='PIntStringStringValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='intValue', full_name='PIntStringStringValue.intValue', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stringValue1', full_name='PIntStringStringValue.stringValue1', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stringValue2', full_name='PIntStringStringValue.stringValue2', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=141,
  serialized_end=286,
)


_PLONGINTINTBYTEBYTESTRINGVALUE = _descriptor.Descriptor(
  name='PLongIntIntByteByteStringValue',
  full_name='PLongIntIntByteByteStringValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='longValue', full_name='PLongIntIntByteByteStringValue.longValue', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='intValue1', full_name='PLongIntIntByteByteStringValue.intValue1', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='intValue2', full_name='PLongIntIntByteByteStringValue.intValue2', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='byteValue1', full_name='PLongIntIntByteByteStringValue.byteValue1', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='byteValue2', full_name='PLongIntIntByteByteStringValue.byteValue2', index=4,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stringValue', full_name='PLongIntIntByteByteStringValue.stringValue', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=289,
  serialized_end=469,
)


_PINTBOOLEANINTBOOLEANVALUE = _descriptor.Descriptor(
  name='PIntBooleanIntBooleanValue',
  full_name='PIntBooleanIntBooleanValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='intValue1', full_name='PIntBooleanIntBooleanValue.intValue1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boolValue1', full_name='PIntBooleanIntBooleanValue.boolValue1', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='intValue2', full_name='PIntBooleanIntBooleanValue.intValue2', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boolValue2', full_name='PIntBooleanIntBooleanValue.boolValue2', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=471,
  serialized_end=577,
)


_PSTRINGSTRINGVALUE = _descriptor.Descriptor(
  name='PStringStringValue',
  full_name='PStringStringValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stringValue1', full_name='PStringStringValue.stringValue1', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stringValue2', full_name='PStringStringValue.stringValue2', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=579,
  serialized_end=703,
)


_PANNOTATIONVALUE = _descriptor.Descriptor(
  name='PAnnotationValue',
  full_name='PAnnotationValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stringValue', full_name='PAnnotationValue.stringValue', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boolValue', full_name='PAnnotationValue.boolValue', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='intValue', full_name='PAnnotationValue.intValue', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longValue', full_name='PAnnotationValue.longValue', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shortValue', full_name='PAnnotationValue.shortValue', index=4,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='doubleValue', full_name='PAnnotationValue.doubleValue', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='binaryValue', full_name='PAnnotationValue.binaryValue', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='byteValue', full_name='PAnnotationValue.byteValue', index=7,
      number=8, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='intStringValue', full_name='PAnnotationValue.intStringValue', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stringStringValue', full_name='PAnnotationValue.stringStringValue', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='intStringStringValue', full_name='PAnnotationValue.intStringStringValue', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longIntIntByteByteStringValue', full_name='PAnnotationValue.longIntIntByteByteStringValue', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='intBooleanIntBooleanValue', full_name='PAnnotationValue.intBooleanIntBooleanValue', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='field', full_name='PAnnotationValue.field',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=706,
  serialized_end=1197,
)


_PANNOTATION = _descriptor.Descriptor(
  name='PAnnotation',
  full_name='PAnnotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='PAnnotation.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='PAnnotation.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1199,
  serialized_end=1259,
)

_PINTSTRINGVALUE.fields_by_name['stringValue'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_PINTSTRINGSTRINGVALUE.fields_by_name['stringValue1'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_PINTSTRINGSTRINGVALUE.fields_by_name['stringValue2'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_PLONGINTINTBYTEBYTESTRINGVALUE.fields_by_name['stringValue'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_PSTRINGSTRINGVALUE.fields_by_name['stringValue1'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_PSTRINGSTRINGVALUE.fields_by_name['stringValue2'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_PANNOTATIONVALUE.fields_by_name['intStringValue'].message_type = _PINTSTRINGVALUE
_PANNOTATIONVALUE.fields_by_name['stringStringValue'].message_type = _PSTRINGSTRINGVALUE
_PANNOTATIONVALUE.fields_by_name['intStringStringValue'].message_type = _PINTSTRINGSTRINGVALUE
_PANNOTATIONVALUE.fields_by_name['longIntIntByteByteStringValue'].message_type = _PLONGINTINTBYTEBYTESTRINGVALUE
_PANNOTATIONVALUE.fields_by_name['intBooleanIntBooleanValue'].message_type = _PINTBOOLEANINTBOOLEANVALUE
_PANNOTATIONVALUE.oneofs_by_name['field'].fields.append(
  _PANNOTATIONVALUE.fields_by_name['stringValue'])
_PANNOTATIONVALUE.fields_by_name['stringValue'].containing_oneof = _PANNOTATIONVALUE.oneofs_by_name['field']
_PANNOTATIONVALUE.oneofs_by_name['field'].fields.append(
  _PANNOTATIONVALUE.fields_by_name['boolValue'])
_PANNOTATIONVALUE.fields_by_name['boolValue'].containing_oneof = _PANNOTATIONVALUE.oneofs_by_name['field']
_PANNOTATIONVALUE.oneofs_by_name['field'].fields.append(
  _PANNOTATIONVALUE.fields_by_name['intValue'])
_PANNOTATIONVALUE.fields_by_name['intValue'].containing_oneof = _PANNOTATIONVALUE.oneofs_by_name['field']
_PANNOTATIONVALUE.oneofs_by_name['field'].fields.append(
  _PANNOTATIONVALUE.fields_by_name['longValue'])
_PANNOTATIONVALUE.fields_by_name['longValue'].containing_oneof = _PANNOTATIONVALUE.oneofs_by_name['field']
_PANNOTATIONVALUE.oneofs_by_name['field'].fields.append(
  _PANNOTATIONVALUE.fields_by_name['shortValue'])
_PANNOTATIONVALUE.fields_by_name['shortValue'].containing_oneof = _PANNOTATIONVALUE.oneofs_by_name['field']
_PANNOTATIONVALUE.oneofs_by_name['field'].fields.append(
  _PANNOTATIONVALUE.fields_by_name['doubleValue'])
_PANNOTATIONVALUE.fields_by_name['doubleValue'].containing_oneof = _PANNOTATIONVALUE.oneofs_by_name['field']
_PANNOTATIONVALUE.oneofs_by_name['field'].fields.append(
  _PANNOTATIONVALUE.fields_by_name['binaryValue'])
_PANNOTATIONVALUE.fields_by_name['binaryValue'].containing_oneof = _PANNOTATIONVALUE.oneofs_by_name['field']
_PANNOTATIONVALUE.oneofs_by_name['field'].fields.append(
  _PANNOTATIONVALUE.fields_by_name['byteValue'])
_PANNOTATIONVALUE.fields_by_name['byteValue'].containing_oneof = _PANNOTATIONVALUE.oneofs_by_name['field']
_PANNOTATIONVALUE.oneofs_by_name['field'].fields.append(
  _PANNOTATIONVALUE.fields_by_name['intStringValue'])
_PANNOTATIONVALUE.fields_by_name['intStringValue'].containing_oneof = _PANNOTATIONVALUE.oneofs_by_name['field']
_PANNOTATIONVALUE.oneofs_by_name['field'].fields.append(
  _PANNOTATIONVALUE.fields_by_name['stringStringValue'])
_PANNOTATIONVALUE.fields_by_name['stringStringValue'].containing_oneof = _PANNOTATIONVALUE.oneofs_by_name['field']
_PANNOTATIONVALUE.oneofs_by_name['field'].fields.append(
  _PANNOTATIONVALUE.fields_by_name['intStringStringValue'])
_PANNOTATIONVALUE.fields_by_name['intStringStringValue'].containing_oneof = _PANNOTATIONVALUE.oneofs_by_name['field']
_PANNOTATIONVALUE.oneofs_by_name['field'].fields.append(
  _PANNOTATIONVALUE.fields_by_name['longIntIntByteByteStringValue'])
_PANNOTATIONVALUE.fields_by_name['longIntIntByteByteStringValue'].containing_oneof = _PANNOTATIONVALUE.oneofs_by_name['field']
_PANNOTATIONVALUE.oneofs_by_name['field'].fields.append(
  _PANNOTATIONVALUE.fields_by_name['intBooleanIntBooleanValue'])
_PANNOTATIONVALUE.fields_by_name['intBooleanIntBooleanValue'].containing_oneof = _PANNOTATIONVALUE.oneofs_by_name['field']
_PANNOTATION.fields_by_name['value'].message_type = _PANNOTATIONVALUE
DESCRIPTOR.message_types_by_name['PIntStringValue'] = _PINTSTRINGVALUE
DESCRIPTOR.message_types_by_name['PIntStringStringValue'] = _PINTSTRINGSTRINGVALUE
DESCRIPTOR.message_types_by_name['PLongIntIntByteByteStringValue'] = _PLONGINTINTBYTEBYTESTRINGVALUE
DESCRIPTOR.message_types_by_name['PIntBooleanIntBooleanValue'] = _PINTBOOLEANINTBOOLEANVALUE
DESCRIPTOR.message_types_by_name['PStringStringValue'] = _PSTRINGSTRINGVALUE
DESCRIPTOR.message_types_by_name['PAnnotationValue'] = _PANNOTATIONVALUE
DESCRIPTOR.message_types_by_name['PAnnotation'] = _PANNOTATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PIntStringValue = _reflection.GeneratedProtocolMessageType('PIntStringValue', (_message.Message,), {
  'DESCRIPTOR' : _PINTSTRINGVALUE,
  '__module__' : 'Annotation_pb2'
  # @@protoc_insertion_point(class_scope:PIntStringValue)
  })
_sym_db.RegisterMessage(PIntStringValue)

PIntStringStringValue = _reflection.GeneratedProtocolMessageType('PIntStringStringValue', (_message.Message,), {
  'DESCRIPTOR' : _PINTSTRINGSTRINGVALUE,
  '__module__' : 'Annotation_pb2'
  # @@protoc_insertion_point(class_scope:PIntStringStringValue)
  })
_sym_db.RegisterMessage(PIntStringStringValue)

PLongIntIntByteByteStringValue = _reflection.GeneratedProtocolMessageType('PLongIntIntByteByteStringValue', (_message.Message,), {
  'DESCRIPTOR' : _PLONGINTINTBYTEBYTESTRINGVALUE,
  '__module__' : 'Annotation_pb2'
  # @@protoc_insertion_point(class_scope:PLongIntIntByteByteStringValue)
  })
_sym_db.RegisterMessage(PLongIntIntByteByteStringValue)

PIntBooleanIntBooleanValue = _reflection.GeneratedProtocolMessageType('PIntBooleanIntBooleanValue', (_message.Message,), {
  'DESCRIPTOR' : _PINTBOOLEANINTBOOLEANVALUE,
  '__module__' : 'Annotation_pb2'
  # @@protoc_insertion_point(class_scope:PIntBooleanIntBooleanValue)
  })
_sym_db.RegisterMessage(PIntBooleanIntBooleanValue)

PStringStringValue = _reflection.GeneratedProtocolMessageType('PStringStringValue', (_message.Message,), {
  'DESCRIPTOR' : _PSTRINGSTRINGVALUE,
  '__module__' : 'Annotation_pb2'
  # @@protoc_insertion_point(class_scope:PStringStringValue)
  })
_sym_db.RegisterMessage(PStringStringValue)

PAnnotationValue = _reflection.GeneratedProtocolMessageType('PAnnotationValue', (_message.Message,), {
  'DESCRIPTOR' : _PANNOTATIONVALUE,
  '__module__' : 'Annotation_pb2'
  # @@protoc_insertion_point(class_scope:PAnnotationValue)
  })
_sym_db.RegisterMessage(PAnnotationValue)

PAnnotation = _reflection.GeneratedProtocolMessageType('PAnnotation', (_message.Message,), {
  'DESCRIPTOR' : _PANNOTATION,
  '__module__' : 'Annotation_pb2'
  # @@protoc_insertion_point(class_scope:PAnnotation)
  })
_sym_db.RegisterMessage(PAnnotation)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)