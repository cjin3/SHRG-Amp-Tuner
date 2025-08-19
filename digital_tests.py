import numpy as np
import scipy.fft as fft
import matplotlib.pyplot as plt

def test():
    freq = 40
    sine_wave(freq)
    graph()
    

def sine_wave(frequency): 
    #frequency in hertz
    duration = 1/40
    sample_timer = np.linspace(0, duration, frequency//2, False)
    wave = np.sin(frequency*2*np.pi*sample_timer)
    plt.plot(sample_timer, wave)
    return wave

def graph():
    plt.grid()
    plt.show()

test()