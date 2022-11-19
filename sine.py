# Generates a single sine wave period with N samples at the specified sample width (in bytes)
import numpy as np

def sine(N, sample_width):
	print("Generating sine...")
	scale = 2**(sample_width*8-1)
	wave_table = np.array([scale*np.sin(2*np.pi*(i/N)) for i in range(N)], dtype=np.int32)	
	wave_table = wave_table.astype(int)
	return wave_table
