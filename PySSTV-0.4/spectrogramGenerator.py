import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile

def spectra(path_to_wav):
    sample_rate, samples = wavfile.read(path_to_wav)
    frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

    plt.pcolormesh(times, frequencies, spectrogram)
    #plt.imshow(spectrogram)
    plt.ylabel("Frequency [Hz]")
    plt.xlabel("Time [sec]")
    plt.show()
