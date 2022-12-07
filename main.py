from sawtooth import *
from sine import *
from square import *
from custom import *
from file_gen import *

import numpy as np
import os

print("Enter the number of the waveform you want to generate:")
x = int(input("Sinusoid (1)    Sawtooth (2)    Square (3)    All of them (4)    Convert my own wav file to samples (5): "))
if x < 1 or x > 5:
	print("Not an option, sorry!")
	exit()
if x == 5:
	print("Make sure all of your desired wav files are located in the input_files directory")
	
sample_depth = int(input("How many bytes (not bits) do you want per sample?: "))
if sample_depth > 3:
	print("Sample Depth too big! setting it to the maximum of 3 bytes")
	sample_depth = 3

if sample_depth < 1:
	print(f"I'm not sure how to generate {sample_depth} byte samples!")
	exit()

if x >= 1 and x <= 4:
	N = int(input("How many samples do you want in your wave table (recommend 4096, or some large power of 2): "))	
	print(f"You will need a {int(np.ceil(np.log2(N)))} bit counter to index into your wave table")


if x == 1 or x == 4:
	data = sine(N, sample_depth)
	file_gen(data, "sine", N, sample_depth)

if x == 2 or x == 4:
	data = sawtooth_bl(N, sample_depth)
	file_gen(data, "sawtooth", N, sample_depth)

if x == 3 or x == 4:
	data = square_bl(N, sample_depth)
	file_gen(data, "square", N, sample_depth)	


if x == 5:
	for filename in os.listdir("input_files"):	
		if (".wav" not in filename):
			continue
		data = custom(filename, sample_depth)
		if len(data) < 1:
			continue
		file_gen(data, filename.replace(".wav", ""), len(data), sample_depth)
	


print("Generated txt and png files of your waveforms to output_files directory")
