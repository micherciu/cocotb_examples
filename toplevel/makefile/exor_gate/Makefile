# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0

# Makefile

# defaults
SIM ?= icarus
WAVES=1
TOPLEVEL_LANG ?= verilog

# use VERILOG_SOURCES for Verilog files
VERILOG_SOURCES += ${PWD}/../../../modules/exor_gate_fm.v

# use VHDL_SOURCES for VHDL files

# COCOTB_TOPLEVEL or TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
# for version < 2.0
#TOPLEVEL = exor_gate_fm 

# version >= 2.0
COCOTB_TOPLEVEL = exor_gate_fm

# COCOTB_TEST_MODULES or MODULE is the basename of the Python test file(s)
# for version < 2.0
#MODULE = and_gate_tb

# version >= 2.0
COCOTB_TEST_MODULES = exor_gate_tb

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim

cleanall:
	rm -r results.xml __pycache__ sim_build
