# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0
# quick_start_tb.py

import cocotb
from cocotb.triggers import FallingEdge, Timer

async def generate_clock(dut):
    """Generate clock pulses."""

    for cycle in range(10):
        dut.clk.value = 0
        await Timer(1, unit="ns")
        dut.clk.value = 1
        await Timer(1, unit="ns")


@cocotb.test()
async def quick_start(dut):
    """Try accessing the design."""

    await cocotb.start(generate_clock(dut))  # run the clock "in the background"

    await Timer(5, unit="ns")  # wait a bit
    await FallingEdge(dut.clk)  # wait for falling edge/"negedge"

    dut._log.info("my_signal_1 is %s", dut.my_signal_1.value)
    dut.my_signal_1.value = 1

    await Timer(5, unit="ns")  # wait a bit
    await FallingEdge(dut.clk)  # wait for falling edge/"negedge"

    dut._log.info("my_signal_1 is %s", dut.my_signal_1.value)
    dut.my_signal_2.value = 1
    dut.my_signal_1.value = 0

    await Timer(5, unit="ns")  # wait a bit
    await FallingEdge(dut.clk)  # wait for falling edge/"negedge"
    dut.my_signal_2.value = 0
    dut.my_signal_1.value = 0
