#!/usr/bin/env python

import sys
import numpy as np
from scipy.io import wavfile
from scipy import signal
from notes import pitch, piano_freq, freq_dict, my_spectrogram
import pandas as pd
import matplotlib.pyplot as plt

if len(sys.argv) < 2:
    print("Usage: python spectrogram.py <myAwesomeTrack.wav>")
    sys.exit(0)

FNAME = sys.argv[1]

### Read a wavfile
(fs, x) = wavfile.read(FNAME)
if x.ndim > 1:
    x = x[:,1]

# TEST
#f, t, S = signal.spectrogram(x, fs, nperseg=2**14, noverlap=2**14*.5, window=signal.get_window('blackman', Nx=2**14))

### Spectrogram (High resolution)
# nperseg = 2 ** 14
# f, t, Zxx = my_spectrogram(x, fs, nperseg=nperseg, noverlap=nperseg / 2)
nperseg = 2 ** 13
f, t, Zxx = my_spectrogram(x, fs, nperseg=nperseg, noverlap=nperseg / 8)

if False:
    idx = np.argwhere(f <= 4200).squeeze()
    plt.pcolormesh(t, f[idx], np.abs(Zxx[idx, :]))
    plt.title('STFT Magnitude')
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.colorbar()
    plt.show()

### Dump JSON ###
index = [p.replace('#', 's') for p in pitch(f)]
df = pd.DataFrame(Zxx, index=index, columns=np.round(t,2))
json = df.to_json() # indexed by time, then by freq.
json = "[" + json + "]"

with open("tmp/spec.json", 'w+') as f: 
    f.write(json)
    f.close()

