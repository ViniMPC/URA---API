import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

class recorder:
    def __init__(self, temp, freq, channels):
        self.temp = temp
        self.freq = freq
        self.channels = channels

    def record_audio(self, filename, device=None):
        """
        Record audio from specified device.
        device: None (default), int (device ID), or 'internal'/'external'
        """
        print("Recording...")
        try:
            recording = sd.rec(int(self.temp * self.freq), samplerate=self.freq, channels=self.channels, device=device)
            sd.wait()
            print("Recording complete.")
            write(filename, self.freq, recording)
            wv.write(filename, recording, self.freq, sampwidth=2)  
            print(f"Audio saved as {filename}")
        except Exception as e:
            print(f"Error recording audio: {e}")

    def list_devices(self):
        """List available audio devices"""
        print(sd.query_devices())

    def record_internal(self, filename):
        """Record from internal microphone"""
        print("Recording from internal device...")
        self.record_audio(filename, device=0)

    def record_external(self, filename, device_id=1):
        """Record from external device"""
        print(f"Recording from external device {device_id}...")
        self.record_audio(filename, device=device_id)
        recording = sd.rec(int(self.temp * self.freq), samplerate=self.freq, channels=self.channels)
        sd.wait()
        print("Recording complete.")
        write(filename, self.freq, recording)
        wv.write(filename, recording, self.freq, sampwidth=2)  
        print(f"Audio saved as {filename}")