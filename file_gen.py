import matplotlib.pyplot as plt
import numpy as np

def file_gen(data, name, N, sample_depth):	
	plt.figure()
	plt.plot(data)
	plt.savefig(f"output_files/{name}.png")
	with open(f'output_files/{name}.txt', 'w') as file:
		for i in data:
			file.write(hex(i).replace('0x', ''))
			file.write("\n")

	with open(f'output_files/{name}.sv', 'w') as file:
		file.write(f"module {name}_rom (\ninput clk,\ninput [{int(np.ceil(np.log2(N)))-1}:0] addr,\n")
		file.write(f"output logic [{8*sample_depth-1}:0] q\n)\n\n")
		file.write(f"logic [{8*sample_depth-1}:0] rom [{N}];\n")
		file.write("always_ff @(posedge clk) begin\n")
		file.write("	q <= rom[addr];\n")
		file.write("end\n")
		file.write(f"initial begin $readmemh(\"{name}.txt\", rom); end\n")
		file.write("endmodule")
