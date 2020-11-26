import sounddevice as sd
import numpy as np
import scipy.fft
import matplotlib.pyplot as plt

fs = 48000
duration = 10
print(sd.default.device)
print(sd.query_devices())
recording = 0

def callback(indata, frames, time, status):
  if status:
    print(status)

  peakLocation(indata)

def peakLocation(indata):
  Y = np.abs(indata)  # Find magnitude
  list = []
  peakY = np.max(Y)  # Find max peak
  list.append(peakY)
  locY = np.argmax(Y)  # Find its location
  #frqY = frq[locY]  # Get the actual frequency value



  array = scipy.fft.rfft(indata)
  print("Audio data: ")
  print(indata)

  print("FFT af audio data: ")
  print(array)



  plt.xlabel('Time')
  plt.ylabel('Amplitude')
  plt.plot(indata)
  plt.show()

with sd.InputStream(channels=2, callback=callback, samplerate = fs):
    sd.sleep(1000*duration)
