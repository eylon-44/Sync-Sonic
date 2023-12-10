# constants.py stores category based constants

class AudioConsts():

    VOLUME               = 0.5         # speaker's volume :: ranging from 0.0 to 1.0
    MIN_FREQUENCY        = 100         # minimum frequency to be played/listen to
    MAX_FREQUENCY        = 20000       # maximum frequency to be played/listen to
    SAMPLE_RATE          = 44100       # sample rate
    BEAPS_OUT_PER_SECOND = 5           # number of fixed frequency sounds to be played in a second
    BEAPS_IN_PER_SECOND  = 20          # number of fixed frequency sounds to be listen to in a second