from utils.constants import AudioConsts
from .microphone import Microphone
from .speaker    import Speaker

from typing import Tuple, List
import sys

class Network():
    '''
        Static class for sending and recieving data bytes using the [Microphone] and [Speaker] interfaces
        The class must be initiated by calling the [Network.init] function before using it
    '''

    # Initiate speaker and microphone
    @staticmethod
    def init():
        Microphone.init()
        Speaker.init()

    # Listen for an array of [size] bytes using the microphone :: return a list of tuple (volume, byte)
    @staticmethod
    def input(size: int) -> List[ Tuple[int, bytes] ]:
        data: List[ Tuple[int, bytes] ] = list()

        # record audio bytes [size] times
        for i in range(size):
            # record: get volume and frequency
            volume, frequency = Microphone.record()

            # if frequency is in range
            if frequency >= AudioConsts.MIN_FREQUENCY and frequency <= AudioConsts.MAX_FREQUENCY:
                # convert frequency to byte data
                byte_value = round((frequency - AudioConsts.MIN_FREQUENCY) / ((AudioConsts.MAX_FREQUENCY - AudioConsts.MIN_FREQUENCY) / 256))
            else:
                volume = byte_value = 0

            byte = byte_value.to_bytes(int((byte_value.bit_length() + 7) / 8), 'big')
            data.append((volume, byte))

        return data

    # Output an array of bytes using the speaker
    @staticmethod
    def output(data: bytes) -> None:
        for i in range(len(data)):
            
            # print the data to screen [TEMP][DEBUG]
            frequency  = int(AudioConsts.MIN_FREQUENCY + ((AudioConsts.MAX_FREQUENCY - AudioConsts.MIN_FREQUENCY) / 256) * data[i])
            print(f'{frequency}: {data.decode()[i]} [{ord(data.decode()[i])}]')
            sys.stdout.flush()

            # convert byte value to frequency and play it using the speaker
            frequency  = int(AudioConsts.MIN_FREQUENCY + ((AudioConsts.MAX_FREQUENCY - AudioConsts.MIN_FREQUENCY) / 256) * data[i])
            Speaker.play(frequency)

    def __to_bytes():
        pass