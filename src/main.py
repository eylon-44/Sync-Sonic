''' 
Sync-Sonic Program 

Repo:  	https://github.com/eylon-44/Sync-Sonic
Author: Eylon | https://github.com/eylon-44
'''

from hardware import Speaker

def main():
	Speaker.init()		# initiate the speaker
	return 0

if (__name__ == '__main__'):
	main()
