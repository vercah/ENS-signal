import numpy as np
import wave as wv
import matplotlib.pyplot as plt


def load_sound(file, n0=None):
    
    x_raw = wv.open(file)
    n = x_raw.getnframes()
    x = np.fromstring(x_raw.readframes(-1), np.int16)
    x_raw.close()
    
    if file[::-1][:8][::-1] == "bird.wav":
        x = np.delete(x,list(range(6001)) + list(range(12500, 15001)) + list(range(22500, 24001)) + list(range(32500,34001)))

    if n0==None :
        x=x
    elif n0 !=0 and n0 < n:
        x = x[:n0]
    
    return x/np.max(x)

def fourier_transform(signal,Fe):
    pass

def fourier_transform_positif(signal,Fe):
    pass

def inverse_fourier_transform(FT,Fe):
    pass

def define_times(n,Fe):
    pass

def low_pass(Y,freq,fc):
    pass
    
def high_pass(Y,freq,fc):
    pass
    
def band_stop(Y,freq,fc1,fc2):
    pass

def band_pass(Y,freq,fc1,fc2):
    pass


