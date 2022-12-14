# Generates a band-limited sawtooth period of N samples
import numpy as np

def sawtooth_bl(N, sample_width):
	print("Generating sawtooth...")
	n = 50 # number of harmonics in fourier series
	scale = 2**(sample_width*8-1)-1
	wave_table = [0]*N
	for k in range(1, n):
		wave_table = np.add(wave_table, [1/k*np.sin(2*np.pi*(k*x/N)) for x in range(N)])	
	wave_table = np.array(list(map(lambda i:(i-min(wave_table))/max(wave_table)*scale-scale, wave_table)), dtype=np.int32)
	wave_table = wave_table.astype(int)

	return wave_table

