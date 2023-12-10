from utils.constants import AudioConsts

import pyaudio
import numpy
from typing import Tuple

class Microphone():
    '''
        The Microphone class provides an interface for using the microphone and getting volume and frequency data from it
        The class must be initiated by calling the [Microphone.init] function before using it
    '''

    __recording_format = pyaudio.paInt16                                        # recording format
    __chunk = int(AudioConsts.SAMPLE_RATE * (1/AudioConsts.BEAPS_IN_PER_SECOND))   # buffer size per read

    @classmethod
    def init(cls) -> None:
        cls.__recorder = pyaudio.PyAudio()
        cls.__stream = cls.__recorder.open(format=cls.__recording_format,
                channels=1,
                rate=AudioConsts.SAMPLE_RATE, input=True,
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
        current_freq = int(dominant_freq * AudioConsts.SAMPLE_RATE / cls.__chunk)

        #print(f"Volume: {volume}, Frequency: {current_freq} Hz")
        return (volume, current_freq)

    # At exit, terminate the audio player and stop and close the audio stream
    @classmethod
    def __atexit(cls) -> None:
        # terminate the audio player
        cls.__recorder.terminate()
        # stop and close the audio stream
        cls.stream.stop_stream()
        cls.stream.close()