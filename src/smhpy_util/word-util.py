import os









def number_word(num):
	if num < 20:
		nw = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
		return nw[num]
	tens = num // 10
	ones = num % 10
	ts = ['0x','1x','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
	s = ts[tens]
	if ones > 0:
		s += '-'
		s += number_word(ones)
	return s

def write_numbers():
	for i in range(100):
		print(number_word(i))

if __name__ == '__main__':
	print('word-util')
	#test_unicode_accents()
	write_numbers()