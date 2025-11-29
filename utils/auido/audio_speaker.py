import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

class recorder:
    def __init__(self, temp, freq, channels):
        self.temp = temp
        self.freq = freq
        self.channels = channels

    def record_audio(self, filename):
        print("Recording...")
        recording = sd.rec(int(self.temp * self.freq), samplerate=self.freq, channels=self.channels)
        sd.wait()
        print("Recording complete.")
        write(filename, self.freq, recording)
        wv.write(filename, recording, self.freq, sampwidth=2)  
        print(f"Audio saved as {filename}")