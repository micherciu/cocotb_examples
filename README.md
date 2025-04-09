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

### 2. Using Makefile:  
* Compilation using makefile
    * define/change/write
        - Makefile
        - HDL description file (Verilog/VHDL)
        - Test bench file (python)
    * command
        `make`

### 3. Using Runner:  
* Compilation using python
    * define/change/write
        - Runner (python specific file)
        - HDL description file (Verilog/VHDL)
        - Test bench file (python)
    * command:
        `python runner_file_name.py`

### 4. Verilog Modules:
*  Quick simple

### 5. Folder Structure:

```mermaid 
graph TD;
    cocotb_examples-->.git;
    cocotb_examples-->README.md;
    cocotb_examples-->modules;
    modules-->Quick_simple
    cocotb_examples-->toplevel;
    toplevel-->makefile;
    toplevel-->runner;
```

### 6. References:
* https://www.cocotb.org/
* https://www.python.org/
* https://pypi.org/project/pip/
* https://www.chipverify.com/tutorials/verilog
* https://nandland.com/

