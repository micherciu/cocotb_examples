# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0

# and_gate_tb.py (simple)

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer


@cocotb.test()
async def and_gate_fm(dut):
    """Try accessing the design."""

    clock = Clock(dut.clk, 2, unit="ns") 
    cocotb.start_soon(clock.start())

    dut._log.info("a signal is %s", dut.a.value)
    dut.a.value = 0
    await Timer(5, unit="ns")  # wait a bit
    dut._log.info("b signal is %s", dut.b.value)
    dut.b.value = 1
    await Timer(5, unit="ns")  # wait a bit
    dut._log.info("a signal is %s", dut.a.value)
    dut.a.value = 1
    await Timer(5, unit="ns")  # wait a bit
    dut._log.info("b signal is %s", dut.b.value)
    dut.b.value = 0
    await Timer(5, unit="ns")  # wait a bit