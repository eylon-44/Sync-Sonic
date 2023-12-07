import pyaudio, numpy
import atexit

class Speaker():
    '''
        The Speaker class provides an interface for playing fixed frequency sounds for a selected duration
        The class must be initiated by calling the [Speaker.init] function before using it
    '''

    __volume = 0.5            # speaker volume :: [0.0 - 1.0] range
    __sample_rate = 44100     # audio sample rate

    # Initiate the speaker
    @classmethod
    def init(cls):
        # initialize a port audio player
        cls.__player = pyaudio.PyAudio()

        # open and start an audio output stream
        cls.stream = cls.__player.open(format=pyaudio.paFloat32,
                channels=1,
                rate=cls.__sample_rate,
                output=True)
        cls.stream.start_stream()

        # set an atexit function for the speaker
        atexit.register(cls.__atexit)

    # Play a fixed frequency for [duration] milliseconds
    @classmethod
    def play(cls, freq: int, duration: int):
        # calculate the number of samples needed based on the sample rate and duration
        sample_count = int(Speaker.__sample_rate * duration / 1000)

        # generate an array of time values representing the duration of the audio snippet
        time_values = numpy.linspace(0, duration / 1000, sample_count, endpoint=False)
        
        # generate audio signal using a sine wave formula
        audio_data = Speaker.__volume * numpy.sin(2 * numpy.pi * freq * time_values)

        # write the audio data to the output stream for playback
        cls.stream.write(audio_data.astype(numpy.float32).tobytes())
               
    # At exit, terminate the audio player and stop and close the audio stream
    @classmethod
    def __atexit(cls):
        # terminate the audio player
        cls.__player.terminate()
        # stop and close the audio stream
        cls.stream.stop_stream()
        cls.stream.close()