# -*- coding: utf-8 -*-
# MIT License
#
# Copyright (c) 2022 Quandela
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# flake8: noqa

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: perceval_circuit.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16perceval_circuit.proto\x12\x0fperceval.schema\"<\n\rComplexDouble\x12\x12\n\nreal_value\x18\x01 \x01(\x01\x12\x17\n\x0fimaginary_value\x18\x02 \x01(\x01\"Q\n\tParameter\x12\x14\n\nreal_value\x18\x01 \x01(\x01H\x00\x12\x10\n\x06symbol\x18\x02 \x01(\tH\x00\x12\x14\n\nexpression\x18\x03 \x01(\tH\x00\x42\x06\n\x04type\"<\n\x0cMatrixDouble\x12,\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x1e.perceval.schema.ComplexDouble\":\n\x0eMatrixSymbolic\x12(\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x1a.perceval.schema.Parameter\"\x93\x01\n\x06Matrix\x12\x0c\n\x04rows\x18\x01 \x01(\x05\x12\x0c\n\x04\x63ols\x18\x02 \x01(\x05\x12\x30\n\x07numeric\x18\x03 \x01(\x0b\x32\x1d.perceval.schema.MatrixDoubleH\x00\x12\x33\n\x08symbolic\x18\x04 \x01(\x0b\x32\x1f.perceval.schema.MatrixSymbolicH\x00\x42\x06\n\x04\x64\x61ta\"\xc5\x05\n\tComponent\x12\x15\n\rstarting_mode\x18\x01 \x01(\x05\x12\x0e\n\x06n_mode\x18\x02 \x01(\x05\x12\x10\n\x08offset_x\x18\x03 \x01(\x01\x12\x12\n\nannotation\x18\x04 \x01(\t\x12+\n\x07\x63ircuit\x18\n \x01(\x0b\x32\x18.perceval.schema.CircuitH\x00\x12\x36\n\rphase_shifter\x18\x0b \x01(\x0b\x32\x1d.perceval.schema.PhaseShifterH\x00\x12\x36\n\rbeam_splitter\x18\x0c \x01(\x0b\x32\x1d.perceval.schema.BeamSplitterH\x00\x12\x33\n\x0bpermutation\x18\x0e \x01(\x0b\x32\x1c.perceval.schema.PermutationH\x00\x12+\n\x07unitary\x18\x0f \x01(\x0b\x32\x18.perceval.schema.UnitaryH\x00\x12\x30\n\nwave_plate\x18\x10 \x01(\x0b\x32\x1a.perceval.schema.WavePlateH\x00\x12\x35\n\x0fhalf_wave_plate\x18\x11 \x01(\x0b\x32\x1a.perceval.schema.WavePlateH\x00\x12\x38\n\x12quarter_wave_plate\x18\x12 \x01(\x0b\x32\x1a.perceval.schema.WavePlateH\x00\x12\x44\n\x14polarization_rotator\x18\x13 \x01(\x0b\x32$.perceval.schema.PolarizationRotatorH\x00\x12\x30\n\ntime_delay\x18\x14 \x01(\x0b\x32\x1a.perceval.schema.TimeDelayH\x00\x12I\n\x17polarized_beam_splitter\x18\x15 \x01(\x0b\x32&.perceval.schema.PolarizedBeamSplitterH\x00\x42\x06\n\x04type\"7\n\x0cPhaseShifter\x12\'\n\x03phi\x18\x01 \x01(\x0b\x32\x1a.perceval.schema.Parameter\"\xcc\x02\n\x0c\x42\x65\x61mSplitter\x12<\n\nconvention\x18\x01 \x01(\x0e\x32(.perceval.schema.BeamSplitter.Convention\x12)\n\x05theta\x18\x02 \x01(\x0b\x32\x1a.perceval.schema.Parameter\x12*\n\x06phi_tl\x18\x03 \x01(\x0b\x32\x1a.perceval.schema.Parameter\x12*\n\x06phi_bl\x18\x04 \x01(\x0b\x32\x1a.perceval.schema.Parameter\x12*\n\x06phi_tr\x18\x05 \x01(\x0b\x32\x1a.perceval.schema.Parameter\x12*\n\x06phi_br\x18\x06 \x01(\x0b\x32\x1a.perceval.schema.Parameter\"#\n\nConvention\x12\x06\n\x02Rx\x10\x00\x12\x06\n\x02Ry\x10\x01\x12\x05\n\x01H\x10\x02\"\x17\n\x15PolarizedBeamSplitter\"W\n\x07Unitary\x12$\n\x03mat\x18\x01 \x01(\x0b\x32\x17.perceval.schema.Matrix\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x18\n\x10use_polarization\x18\x03 \x01(\x08\"#\n\x0bPermutation\x12\x14\n\x0cpermutations\x18\x01 \x03(\x05\"_\n\tWavePlate\x12)\n\x05\x64\x65lta\x18\x01 \x01(\x0b\x32\x1a.perceval.schema.Parameter\x12\'\n\x03xsi\x18\x02 \x01(\x0b\x32\x1a.perceval.schema.Parameter\"@\n\x13PolarizationRotator\x12)\n\x05\x64\x65lta\x18\x01 \x01(\x0b\x32\x1a.perceval.schema.Parameter\"3\n\tTimeDelay\x12&\n\x02\x64t\x18\x01 \x01(\x0b\x32\x1a.perceval.schema.Parameter\"k\n\x07\x43ircuit\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06n_mode\x18\x02 \x01(\x05\x12\x12\n\nannotation\x18\x03 \x01(\t\x12.\n\ncomponents\x18\x04 \x03(\x0b\x32\x1a.perceval.schema.Componentb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'perceval_circuit_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COMPLEXDOUBLE._serialized_start=43
  _COMPLEXDOUBLE._serialized_end=103
  _PARAMETER._serialized_start=105
  _PARAMETER._serialized_end=186
  _MATRIXDOUBLE._serialized_start=188
  _MATRIXDOUBLE._serialized_end=248
  _MATRIXSYMBOLIC._serialized_start=250
  _MATRIXSYMBOLIC._serialized_end=308
  _MATRIX._serialized_start=311
  _MATRIX._serialized_end=458
  _COMPONENT._serialized_start=461
  _COMPONENT._serialized_end=1170
  _PHASESHIFTER._serialized_start=1172
  _PHASESHIFTER._serialized_end=1227
  _BEAMSPLITTER._serialized_start=1230
  _BEAMSPLITTER._serialized_end=1562
  _BEAMSPLITTER_CONVENTION._serialized_start=1527
  _BEAMSPLITTER_CONVENTION._serialized_end=1562
  _POLARIZEDBEAMSPLITTER._serialized_start=1564
  _POLARIZEDBEAMSPLITTER._serialized_end=1587
  _UNITARY._serialized_start=1589
  _UNITARY._serialized_end=1676
  _PERMUTATION._serialized_start=1678
  _PERMUTATION._serialized_end=1713
  _WAVEPLATE._serialized_start=1715
  _WAVEPLATE._serialized_end=1810
  _POLARIZATIONROTATOR._serialized_start=1812
  _POLARIZATIONROTATOR._serialized_end=1876
  _TIMEDELAY._serialized_start=1878
  _TIMEDELAY._serialized_end=1929
  _CIRCUIT._serialized_start=1931
  _CIRCUIT._serialized_end=2038
# @@protoc_insertion_point(module_scope)
