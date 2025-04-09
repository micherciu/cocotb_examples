## Cocotb examples using Verilog/VHDL description language

0. Requirments:  
# Operating system: Linux / Windows / macOS
# A Verilog or VHDL simulator
# python = 3.13.2
# pip = 24.2
# cocotb = 2.0.0.dev0+63054b88

1. Installation of the cocotb
* Install dependencies
# sudo yum install make python3 python3-pip python3-libs

* Install cocotb
# pip install cocotb

*  Check the installation
# cocotb-config --version

2. Using Makefile:  
* Compilation using makefile
# 1. Makefile 
# 2. HDL description file (Verilog/VHDL)
# 3. Python test bench file

3. Using Runner:  
* Compilation using python
# 1. Python specific file: (as a runner) 
# 2. HDL description file (Verilog/VHDL)
# 3. Python test bench file

4. Verilog Modules:
## 1. Quick example

5. Folder Structure:
 ```
cocotb_examples
 ^t^| ^t^` .git
 ^t^| ^t^` README.md
 ^t^| ^t^` modules
 ^t^| ^t^` toplevel
 ^t^b   ^t^| ^t^` 
 ^t^b   ^t^| ^t^` makefile
 ^t^b   ^t^t ^t^` runner
```


