// This file is public domain, it can be freely copied without restrictions.
// SPDX-License-Identifier: CC0-1.0

module quick_start(input logic clk);

  timeunit 1ns;
  timeprecision 1ns;

  output my_signal_1;
  output my_signal_2;

  assign my_signal_1 = 1'b0;
  assign my_signal_2 = 1'b0;

endmodule
