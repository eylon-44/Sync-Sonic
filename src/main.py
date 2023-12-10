''' 
Sync-Sonic Program 

Repo:  	https://github.com/eylon-44/Sync-Sonic
Author: Eylon | https://github.com/eylon-44
'''

from hardware import Network, Speaker
import os

def main():
	Network.init()
	Network.output('Hello world!'.encode())
	input = Network.input(100)

	return 0

if (__name__ == '__main__'):
	main()