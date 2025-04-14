# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0

# Makefile

# defaults
SIM ?= icarus
WAVES=1
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += ${PWD}/../../../modules/quick_start.v
# use VHDL_SOURCES for VHDL files

# COCOTB_TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = quick_start

# COCOTB_TEST_MODULES is the basename of the Python test file(s)
MODULE = quick_start_tb

# include cocotb's make rules to take care of the simulator setup
#include $(sh cocotb-config --makefiles)/Makefile.sim
include $(shell cocotb-config --makefiles)/Makefile.sim

cleanall:
	rm -r results.xml __pycache__ sim_build