module nor_gate_fm(clk,a,y);
    input clk;
    input a;
    input b;
    output y;

    assign a = 1'b0;
    assign b = 1'b0;
    assign y = ~(a | b);
endmodule