# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0

# my_runner.py

import os
from pathlib import Path
from cocotb_tools.runner import get_runner
#from pycocotools.coco import get_runner

def my_runner():
    sim = os.getenv("SIM", "icarus")
    proj_path = Path(__file__).resolve().parent

    sources = [proj_path / "../../../modules/quick_start.v"]

    runner = get_runner(sim)
    runner.build(
        sources     = sources,
        hdl_toplevel="quick_start",
        waves       = True,
        always = True,
    )

    runner.test(
        hdl_toplevel="quick_start",
        test_module="quick_start_tb",
        waves=True
    )

if __name__ == "__main__":
    my_runner()
