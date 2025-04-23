module exnor_gate_fm(clk,a,b,y);
    input clk;
    input a,b;
    output y;

    assign a = 1'b0;
    assign b = 1'b0;
    assign y = ~(a ^ b);
endmodule