from utils.constants import AudioConsts

import pyaudio, numpy
import atexit

class Speaker():
    '''
        The Speaker class provides an interface for playing fixed frequency sounds for a selected duration
        The class must be initiated by calling the [Speaker.init] function before using it
    '''
    
    __recording_format = pyaudio.paFloat32                                                  # recording format
    __sample_count     = int(AudioConsts.SAMPLE_RATE * (1/AudioConsts.BEAPS_OUT_PER_SECOND))    # calculate the number of samples needed per beep in order to play the sound for 1/[BEEPS_PER_SECOND] seconds

    # Initiate the speaker
    @classmethod
    def init(cls) -> None:
        # initialize a port audio player
        cls.__player = pyaudio.PyAudio()

        # open and start an audio output stream
        cls.stream = cls.__player.open(format=cls.__recording_format,
                channels=1,
                rate=AudioConsts.SAMPLE_RATE,
                output=True)
        cls.stream.start_stream()

        # set an atexit function for the speaker
        atexit.register(cls.__atexit)

    # Play a sine wave fixed frequency sound for 1/[BEEPS_PER_SECOND] seconds 
    @classmethod
    def play(cls, freq: int) -> None:
        # generate an array of time values representing the duration of the audio snippet
        time_values = numpy.linspace(0, 1/AudioConsts.BEAPS_OUT_PER_SECOND, cls.__sample_count, endpoint=False)

        # calculate audio data using a sine wave
        audio_data = numpy.sin(2 * numpy.pi * freq * time_values) * AudioConsts.VOLUME

        # write the audio data to the output stream for playback
        cls.stream.start_stream()
        cls.stream.write(audio_data.astype(numpy.float32).tobytes())
        cls.stream.stop_stream()

    # At exit, terminate the audio player and stop and close the audio stream
    @classmethod
    def __atexit(cls) -> None:
        # terminate the audio player
        cls.__player.terminate()
        # stop and close the audio stream
        cls.stream.stop_stream()
        cls.stream.close()