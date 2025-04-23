## Cocotb examples using Verilog/VHDL description language

### 0. Requirments:  
- Operating system: Linux / Windows / macOS
- A Verilog or VHDL simulator
- python = 3.13.2
- pip = 24.2
- cocotb = 2.0.0.dev0+63054b88

### 1. Installation of the cocotb
* Install dependencies
` sudo yum install make python3 python3-pip python3-libs `

* Install cocotb
` pip install cocotb `

*  Check the installation
`cocotb-config --version`

### 2. TEST BENCH
### A. Using Makefile:
* Compilation using makefile
    * define/change/write
        - Makefile
        - Test bench file (python)
```mermaid
flowchart TB;
    subgraph simple[Simple Example]
    direction LR;
        quick_start[Quick start example];
    end;
    subgraph basic[Basic Gates]
    direction LR;
        and_gate[AND GATE];
        or_gate[OR GATE];
        not_gate[NOT GATE];
    end;
    subgraph universal[Universal Gates]
    direction LR;
        nand_gate[NAND GATE];
        nor_gate[NOR GATE];
    end;
    subgraph other[Other Logic Gates]
    direction LR;
        exor_gate[EX-OR GATE];
        exnor_gate[EX-NOR GATE];
    end;
    
    makefile_tb-->simple;
    makefile_tb-->basic;
    makefile_tb-->universal;
    makefile_tb-->other;
```
    * command
        `make`

### B. Using Runner:  
* Compilation using python
    * define/change/write
        - Runner (python specific file)
        - HDL description file (Verilog/VHDL)
        - Test bench file (python)
    * command:
        `python runner_file_name.py`

### 4. Modules: Verilog examples:
* HDL description file (Verilog/VHDL)
    *  [Quick start](./toplevel/makefile/quick_start/README.md)
    *  [AND GATE example](./toplevel/makefile/and_gate/README.md)
    *  [OR GATE example](./toplevel/makefile/or_gate/README.md)
    *  [NOT GATE example](./toplevel/makefile/not_gate/README.md)
    *  [NAND GATE example](./toplevel/makefile/nand_gate/README.md)
    *  [NOR GATE example](./toplevel/makefile/nor_gate/README.md)
    *  [EXOR GATE example](./toplevel/makefile/exor_gate/README.md)
    *  [EXNOR GATE example](./toplevel/makefile/exnor_gate/README.md)

```mermaid
flowchart TB;
    subgraph simple[Simple Example]
        direction LR;
            quick_start[Quick start example];
        end;
    subgraph basic[Basic Gates]
        direction LR;
            and_gate[AND GATE];
            or_gate[OR GATE];
            not_gate[NOT GATE];
    end;
    subgraph universal[Universal Gates]
        direction LR;
            nand_gate[NAND GATE];
            nor_gate[NOR GATE];
    end;
    subgraph other[Other Logic Gates]
        direction LR;
            exor_gate[EX-OR GATE];
            exnor_gate[EX-NOR GATE];
    end;     
    modules-->simple;
    modules-->basic;
    modules-->universal;
    modules-->other;
```


### 5. Folder Structure:

```mermaid 
graph TD;
    cocotb_examples-->.git;
    cocotb_examples-->README.md;
    cocotb_examples-->modules;
    cocotb_examples-->testbench;
    testbench-->makefile;
    testbench-->runner;
```

### 6. References:
* https://www.cocotb.org/
* https://github.com/cocotb/cocotb/tree/master/examples
* https://circuitfever.com/
* https://www.python.org/
* https://pypi.org/project/pip/
* https://www.chipverify.com/tutorials/verilog
* https://nandland.com/

