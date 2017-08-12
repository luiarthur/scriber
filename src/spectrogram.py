#!/usr/bin/env python

import sys
import numpy as np
from scipy.io import wavfile
from scipy import signal
#import matplotlib.pyplot as plt # only if plotting spectrogram in python...
from notes import pitch, piano_freq, freq_dict, my_spectrogram
import pandas as pd

if len(sys.argv) < 2:
    print "Usage: python spectrogram.py <myAwesomeTrack.wav>"
    sys.exit(0)

FILE = sys.argv[1]

### Read a wavfile
(fs, x) = wavfile.read(FILE)
if x.ndim > 1: x = x[:,1]



### Spectrogram (High resolution)
f, t, Zxx = my_spectrogram(x, fs, nperseg=2**15)
#f.size

### Plot Spectrogram
#plt.pcolormesh(t, np.log(f+1E-6), Zxx, vmin=.05, vmax=1, cmap=plt.cm.gist_heat)
#plt.title('STFT Magnitude')
#plt.ylabel('Frequency [Hz]')
#plt.ylim([np.log(f[1]), np.log(f.max())])
#plt.xlabel('Time [sec]')
#plt.yticks(np.log(f+1E-6), pitch(f))
#plt.show()

### Dump JSON ###
index = [p.replace('#', 's') for p in pitch(f)]
df = pd.DataFrame(Zxx, index=index, columns=np.round(t,2))
json = df.to_json() # indexed by time, then by freq.
json = "[" + json + "]"

with open("out/spec.json", 'w+') as f: 
    f.write(json)
    f.close()


