module cocotb_iverilog_dump();
initial begin
    $dumpfile("/home/madalin/root/FPGA-cern/GitTools/MyFPGA/cocotb_examples/toplevel/runner/quick_start/sim_build/quick_start.fst");
    $dumpvars(0, quick_start);
end
endmodule
