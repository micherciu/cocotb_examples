# adder_tb.py

import cocotb
from cocotb.triggers import FallingEdge, Timer


async def generate_clock(dut):
    """Generate clock pulses."""

    for cycle in range(100):
        dut.clk.value = 0
        await Timer(1, unit="ns")
        dut.clk.value = 1
        await Timer(1, unit="ns")


@cocotb.test()
async def and_gate(dut):
    """Try accessing the design."""

    cocotb.start_soon(generate_clock(dut))  # run the clock "in the background"

    await Timer(5, unit="ns")  # wait a bit
    await FallingEdge(dut.clk)  # wait for falling edge/"negedge"
    dut.a._log.info("Setting a signal")
    dut.a.value = 1
#    assert dut.a.value == 1, "a is now 0!"
    
    await Timer(5, unit="ns")  # wait a bit
    await FallingEdge(dut.clk)  # wait for falling edge/"negedge"
    dut.b._log.info("Setting b signal")
    dut.b.value = 1
#    assert dut.select.value == 1, "select is now 0!"

    await Timer(5, unit="ns")  # wait a bit
    await FallingEdge(dut.clk)  # wait for falling edge/"negedge"
    dut.a._log.info("Setting a signal")
    dut.a.value = 0
#    assert dut.a.value == 1, "a is now 0!"
    
    await Timer(5, unit="ns")  # wait a bit
    await FallingEdge(dut.clk)  # wait for falling edge/"negedge"
    dut.b._log.info("Setting b signal")
    dut.b.value = 0
#    assert dut.select.value == 1, "select is now 0!"

    await Timer(5, unit="ns")  # wait a bit
    await FallingEdge(dut.clk)  # wait for falling edge/"negedge"
    dut.b._log.info("Setting b signal")
    dut.b.value = 0
#    assert dut.select.value == 1, "select is now 0!"
