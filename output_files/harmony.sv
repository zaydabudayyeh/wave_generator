module harmony_rom (
input clk,
input [17:0] addr,
output logic [7:0] q
)

logic [7:0] rom [132300];
always_ff @(posedge clk) begin
	q <= rom[addr];
end
initial begin $readmemh("harmony.txt", rom); end
endmodule