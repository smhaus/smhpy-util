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


class LimitedRepeatRandChoice:
	def __init__(self, choices, norep_pct=0.5):
		self.choices = choices
		self.norep_size = int(len(choices) * norep_pct)
		self.recent = []
		print('init range=', self.norep_size)
	
	def add_recent(self, item):
		if len(self.recent) >= self.norep_size:
			self.recent.pop(0)
		self.recent.append(item)
	
	def next(self, exclude=[]):
		a = random.choice(self.choices)
		while a in self.recent or a in exclude:
			a = random.choice(self.choices)
		self.add_recent(a)
		return a
	
	def build_list(self, size, exclude=[]):
		A = []
		for i in range(size):
			A.append(self.next(exclude))
		return A
	
	def build_str(self, size, exclude=[]):
		S = ''
		for i in range(size):
			S += (str(self.next(exclude)))
		return S


if __name__ == '__main__':
	print('rand-util')