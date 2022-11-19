import matplotlib.pyplot as plt

def file_gen(data, name, N, sample_depth):	
	plt.figure()
	plt.plot(data)
	plt.savefig(f"output_files/{name}.png")
	with open(f'output_files/{name}.txt', 'w') as file:
		for i in data:
			file.write(hex(i).replace('0x', ''))
			file.write("\n")
