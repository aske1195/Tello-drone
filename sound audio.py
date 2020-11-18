import sounddevice as sd
import numpy as np
import scipy.fftpack
import os
import matplotlib.pyplot as plt
import copy
from scipy.io.wavfile import write
import simpleaudio as sa

fs = 48000
duration = 7
#sd.default.device = 5,2
#print(sd.query_devices())

def callback(indata, frames, time, status):
  if status:
    print(status)
  sd.play(indata)
  peakLocation(indata)


def peakLocation(indata):
  Y = np.abs(indata)  # Find magnitude
  peakY = np.max(Y)  # Find max peak
  locY = np.argmax(Y)  # Find its location
  #frqY = frq[locY]  # Get the actual frequency value
  sd.play(indata,fs)

  #scaled = np.int32(indata / np.max(np.abs(indata)) * 32767)
  print(indata)

  write('button1.wav', fs, indata)
  filename = 'button1.wav'
  wave_obj = sa.WaveObject.from_wave_file(filename)
  play_obj = wave_obj.play()
  play_obj.wait_done()

  plt.subplot(2, 1, 1)
  plt.xlabel('Freq (Hz)')
  plt.ylabel('|Y(freq)|')
  plt.plot(indata)
  plt.grid('on')
  plt.show()

with sd.InputStream(channels=2, callback=callback, samplerate = fs):
    sd.sleep(1000*duration)