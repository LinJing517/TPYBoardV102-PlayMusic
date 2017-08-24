import wave
from pyb import DAC
dac = DAC(1)
f = wave.open('/sd/test2.wav')
dac.write_timed(f.readframes(f.getnframes()), f.getframerate())