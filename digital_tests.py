import numpy as np
import scipy.fft as fft
import matplotlib.pyplot as plt

def main():
    sine_wave(440, 10000, 40)

def sine_wave(frequency, sample_rate, samples):
    #frequency (Hz, 1/second), sample_rate (samples/second), sample (samples)
    sample_timer = np.linspace(0, samples/sample_rate, samples, False)
    wave = np.sin(frequency*2*np.pi*sample_timer)
    print(sample_timer)
    print(wave)
    plt.plot(sample_timer, wave)
    plt.grid()
    plt.show()
    return wave

main()