import pyaudio
import numpy
from typing import Tuple

class Microphone():

    buffer = []

    # Local variables for audio recording
    __recording_format = pyaudio.paInt16
    __fps = 10                                  # number of frames (bytes) to read (hear) per seconds
    __sample_rate = 44100
    __chunk = int(__sample_rate * (1/__fps))    # buffer size per read

    @classmethod
    def init(cls):
        cls.__recorder = pyaudio.PyAudio()
        cls.__stream = cls.__recorder.open(format=cls.__recording_format,
                channels=1,
                rate=cls.__sample_rate, input=True,
                frames_per_buffer=cls.__chunk)
    
    # record audio for 1/[BEEPS_PER_SECOND] seconds and return a tuple ([volume], [frequency])
    @classmethod
    def record(cls) -> Tuple[int, int]:
        # read microphone's stream buffer
        mic_in = cls.__stream.read(cls.__chunk)

        # convert the audio bytes data to a numpy array for analysis
        audio_data = numpy.frombuffer(mic_in, dtype=numpy.int16)

        # calculate the volume level :: absolute values' average amplitude
        volume = int(numpy.abs(audio_data).mean())

        # apply Fast Fourier Transform (FFT) to get frequency data, calculate dominant and current frequency
        freq_data = numpy.abs( numpy.fft.fft(audio_data) )
        dominant_freq = numpy.argmax(freq_data)
        current_freq = int(dominant_freq * cls.__sample_rate / cls.__chunk)

        # print(f"Volume: {volume}, Frequency: {current_freq} Hz")
        return (volume, current_freq)

    # At exit, terminate the audio player and stop and close the audio stream
    @classmethod
    def __atexit(cls):
        # terminate the audio player
        cls.__recorder.terminate()
        # stop and close the audio stream
        cls.stream.stop_stream()
        cls.stream.close()