import io
import os
from unidecode import unidecode





def read_to_table(filepath, delin='\t', skipheader=False, encoding='utf-8'):
	L = []
	with open(filepath,'rt',encoding=encoding) as f:
		for line in f:
			arr = line.split(delin)
			for i in range(len(arr)):
				arr[i] = arr[i].strip()
			L.append(arr)
	if skipheader:
		L = L[1:]
	return L

def read_to_map(filepath, delin='\t', encoding='utf-8'):
	M = {}
	with open(filepath,'rt',encoding=encoding) as f:
		for line in f:
			kv = line.split(delin)
			if len(kv) == 2:
				key = kv[0].strip()
				val = kv[1].strip()
				M[key] = val
	return M


def write_table_to_file(filename, datatable, header=None, delin='\t', encoding='utf-8', append=False, fill_empty_right=False):
	
	pardir = os.path.split(filename)[0]
	if not os.path.exists(pardir):
		# print('mkdirs',filepath, pardir)
		os.makedirs(pardir)
	
	maxcols = max(map(len ,datatable))
	print('write' ,filename ,maxcols)
	
	mode = 'w'
	if append:
		mode = 'a'
	with io.open(filename, mode, encoding=encoding) as f:
		if header is not None:
			f.write(delin.join(header))
			f.write('\n')
		
		for row in datatable:
			rout = []
			for col in row:
				if col is None:
					rout.append("")
				else:
					rout.append(str(col))
			f.write(delin.join(rout))
			f.write('\n')



def write_row(outobj, arr, delin):
	outstr = delin.join(arr)
	outobj.write(outstr + '\n')


class FileTableMap:
	def __init__(self, filename, keycols, valcols, delin='\t', skipheader=False, encoding='utf-8', lazyload=True):
		self.filename = filename
		self.keycols = keycols
		self.valcols = valcols
		self.delin = delin
		self.skipheader = skipheader
		self.encoding = encoding
		self.datamap = None
		if not lazyload:
			self.datamap = self.get_data_map()
	
	def get_data_map(self):
		if self.datamap is not None:
			return self.datamap
		table = read_to_table(self.filename, self.delin ,self.skipheader ,self.encoding)
		self.datamap = {}
		for row in table:
			keyobj = self.get_cols_object(row ,self.keycols)
			key = self.keystr(keyobj).lower()
			val = self.get_cols_object(row ,self.valcols)
			self.datamap[key] = val
		return self.datamap
	
	
	def get_cols_object(self, row, colindecies):
		if len(colindecies) == 1:
			index = colindecies[0]
			if index >= len(row):
				return None
			return row[index]
		else:
			L = []
			for index in colindecies:
				if index >= len(row):
					L.append(None)
				else:
					L.append(row[index])
			return L
	
	
	def keystr(self, keyobj):
		return unidecode(str(keyobj)).lower()
	
	def lookup_value(self, keyobj):
		# print('lookup key', self.keystr(keyobj).lower())
		return self.get_data_map()[self.keystr(keyobj).lower()]
	
	def has_key(self, keyobj):
		return self.keystr(keyobj).lower() in self.get_data_map()




class FileListCache:
	cache = {}
	
	def __init__(self ,filepath):
		if filepath not in FileListCache.cache:
			L = read_to_list(filepath)
			FileListCache.cache[filepath] = L
		self.L = FileListCache.cache[filepath]
	
	def get_list(self):
		return self.L



if __name__ == '__main__':
	print('datafiles')