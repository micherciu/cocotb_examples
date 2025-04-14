module not_gate_fm(clk,a,b,y);
    input clk;
    input a;
    output y;

    assign a = 1'b0;
    assign y = ~a;
endmodule