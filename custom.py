import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

def custom(filename, sample_depth):
	print(f"Generating waveform for {filename}...")
	scale = 2**(sample_depth*8-1)-1
	samplerate, data = wavfile.read(f'input_files/{filename}')
	if isinstance(data[0], np.ndarray):
		data = list(map(lambda x:int(sum(x)//len(x)), data))
	if not isinstance(data[0], (int, np.int32)):
		print("Something is wrong with your wav file! please make sure it is encoded in linearPCM format and that you have cleared the metadata tags")
		return
	max_ = max(max(data), abs(min(data)))
	data = list(map(lambda x : x/max_, data))	
	if len(data) > samplerate:	
		print(f"{filename} is pretty long!")
		cont = input("Remember that long audio clips (greater than a couple seconds) will not fit on on-chip memory!\nWould you like to proceed anyway (y/n): ")		
		if cont != 'y':
			return
	min_ = min(data)
	max_ = max(max(data), abs(min_))
	wave_table = np.array(list(map(lambda i:((i-min_)/max_*scale-scale), data)))
	wave_table = wave_table.astype(int)
	return wave_table
