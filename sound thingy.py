import sounddevice as sd
import scipy
import numpy as np
from scipy.io import wavfile as wav
from scipy.io.wavfile import write, read
from scipy import fftpack as scfft
from matplotlib import pyplot as plt

minimumVolume = 0
fs = 44100
seconds = 1
#sd.default.device =
#print(sd.query_devices())

def callback(indata, frames, time, status):
    if status:
        print(status)
    sd.wait()
    write('output.wav', fs, indata)

    fs_rate, signal = read("output.wav")
    l_audio = len(signal.shape)
    N = signal.shape[0]
    secs = N / float(fs_rate)
    Ts = 1.0 / fs_rate
    t = scipy.arange(0, secs, Ts)
    FFT = abs(scipy.fft(signal))
    FFT_side = FFT[range(N // 2)]
    freqs = scipy.fftpack.fftfreq(signal.size, t[1] - t[0])
    fft_freqs = np.array(freqs)
    freqs_side = freqs[range(N // 2)]
    fft_freqs_side = np.array(freqs_side)

    volume = np.array(abs(FFT_side))
    audible = np.where(volume > minimumVolume)
    if freqs_side[audible].any():
        HighestAudibleFrequency = max(freqs_side[audible])
        print(HighestAudibleFrequency)

with sd.InputStream(channels=1, callback=callback, samplerate = fs):
    sd.sleep(1000*seconds)