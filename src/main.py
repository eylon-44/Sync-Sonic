''' 
Sync-Sonic Program 

Repo:  	https://github.com/eylon-44/Sync-Sonic
Author: Eylon | https://github.com/eylon-44
'''

from hardware import Speaker, Microphone

def main():
	Speaker.init()		# initiate the speaker
	Microphone.init()   # initiate the microphone

	return 0

if (__name__ == '__main__'):
	main()
