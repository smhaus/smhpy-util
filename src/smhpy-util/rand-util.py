import random
import string
import os



def randstr(length):
	s = ''
	for i in range(length):
		s += random.choice(string.ascii_lowercase)
	return s

def randhex(length):
	s = ''
	for i in range(length):
		s += random.choice('0123456789ABCDEF')
	return s


def randkey(length, blocksize=0):
	keychar = 'ACDEFGHKMNPRTWXY34679'
	s = ''
	for i in range(length):
		s += random.choice(keychar)
		if blocksize > 0 and (i+1) % blocksize == 0 and i+1<length:
			s += '-'
	return s






if __name__ == '__main__':
	print('rand-util')