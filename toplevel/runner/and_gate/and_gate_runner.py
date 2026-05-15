# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0

# and_gate_runner.py

import os
from pathlib import Path
from cocotb_tools.runner import get_runner
#from pycocotools.coco import get_runner

def and_gate_runner():
    sim = os.getenv("SIM", "icarus")
    proj_path = Path(__file__).resolve().parent

    sources = [proj_path / "../../../modules/and_gate_fm.v"]

    runner = get_runner(sim)
    runner.build(
        sources     = sources,
        hdl_toplevel="and_gate_fm",
        waves       = True,
        always = True
    )

    runner.test(
        hdl_toplevel="and_gate_fm",
        test_module="and_gate_tb",
        waves=True
    )

if __name__ == "__main__":
    and_gate_runner()
