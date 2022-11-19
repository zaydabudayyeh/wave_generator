# Wave Generator
Generates audio waveforms in digital format for use with FPGA audio systems.

### Script usage

#### Setup

1) The script was written using Python version 3.9.6. Make sure that you have this version or later installed on your machine.
2) Clone this directory to your computer.

3) There are a few dependencies for script usage. They are listed in the file requirements.txt.

    running the following from inside the cloned repository should automate this for you:

        pip install -r requirements.txt

  

#### Running the script

3) Run the script from your cloned directory:

        python3 main.py
    
4) Select the waveform types you wish to generate (Sine, Square, Sawtooth, or your very own .wav file!) by selecting the corresponding number.

5) The script will generate the necessary .txt files and .sv files to initialize a ROM using on-chip memory.

      *Note that raw audio samples take up a lot of space. Each second of audio will need 44,100 samples, or 44kB with 8-bit sample depth. The DE-10 lite FPGA has only 200KB of on-chip memory available, so you will only be able to get ~4 seconds of non-repeating audio samples*
