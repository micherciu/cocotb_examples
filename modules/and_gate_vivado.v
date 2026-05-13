`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 05/21/2025 03:25:33 AM
// Design Name: 
// Module Name: top
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module and_gate_vivado(
    input clk,
    input rst,
    input a,
    input b,
    output reg c
    );

always@(negedge clk)
    if(rst)
        begin
            assign c= a & b;
        end
    else
        begin
            assign c = 0;
        end

endmodule
