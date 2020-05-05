import io
import os
#from unidecode import unidecode

#encode=ansi reads some accent chars


def read_to_list(filepath, keep_ws=False, encoding='utf-8'):
	"""
	Read file as list of non-empty lines.
	"""
	L = []
	with open(filepath,'rt',encoding=encoding) as f:
		for line in f:
			if not keep_ws:
				line = line.strip()
			if len(line)>0 or keep_ws:
				L.append(line)
	return L



def read_to_string(filepath, encoding='utf-8'):
	rstr = ''
	with open(filepath ,'rt' ,encoding=encoding) as f:
		for line in f:
			rstr += line
	return rstr

def write_to_file(filepath, text, encoding='utf-8', append=False):
	# pardir = os.path.pardir(filepath)
	pardir = os.path.split(filepath)[0]
	if not os.path.exists(pardir):
		# print('mkdirs',filepath, pardir)
		os.makedirs(pardir)
	mode = 'w'
	if append:
		mode = 'a'
	with io.open(filepath, mode, encoding=encoding) as f:
		f.write(text)


def write_list_to_file(filepath, L, encoding='utf-8', append=False):
	pardir = os.path.split(filepath)[0]
	if not os.path.exists(pardir):
		# print('mkdirs',filepath, pardir)
		os.makedirs(pardir)
	mode = 'w'
	if append:
		mode = 'a'
	with io.open(filepath, mode, encoding=encoding) as f:
		for line in L:
			f.write(line)
			f.write('\n')




if __name__ == '__main__':
	print('fileio')
	#read_to_list()