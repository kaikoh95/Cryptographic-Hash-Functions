import sys
import os
import random
import time
from binascii import unhexlify
from Crypto.Hash import MD5

def long_to_bytes(data):
	#Convert long integer to bytes
	width = data.bit_length()
    	width += 8 - ((width % 8) or 8)
    	fmt = '%%0%dx' % (width // 4)
    	s = unhexlify(fmt % data)
    	return s

def add(data):
	#Convert bytes to long integer and perform add 1
	data = sum(ord(c) << (i * 8) for i, c in enumerate(data[::-1])) + 1
	return long_to_bytes(data)

def compare(a, b, tlen):
	#Compare the first tlen characters (tlen/2 bytes) of a and b
	for i in range(0, tlen):
		if a[i] != b[i]:
			return 1
	return 0

def display(data, slen, elen):
	for i in range(slen, elen):
		print(data[i].encode('hex')),

def avg(stat, count):
	t = 0.0
	for i in stat:
		t += i
	return t/count

if __name__ == '__main__':
	if len(sys.argv) < 2:
		pring("Usage: owb AttemptCount")
		sys.exit(1)

	attempt = int(sys.argv[1])
	count = 0
	statistics = []

	while count < attempt:
		target = os.urandom(16)
		data = os.urandom(32)

		c = 0 #store how many attemps has done for one specific hash value

		h = MD5.new()
		h.update(target)
		target_hash = h.hexdigest()
		h.update(data)
		data_hash = h.hexdigest()
		
		while compare(target_hash, data_hash, 6):
			data = add(data)
			h.update(data)
			data_hash = h.hexdigest()
			c += 1

		print("* Hash value Match: tried for {} times".format(c))
		print("  Original message:"),
		display(target, 0, 16)
		print("\n"),
		print(" Generated message:"),
		display(data, 0, 16)
		print("\n"),
		print("                   "),
		display(data, 16, 32)		
		print("\n"),
		print("     Hash Value:   "), 
		print(target_hash[0:2] + " " + target_hash[2:4] + " " + target_hash[4:6])
		statistics.append(c)
		count += 1

	avg_time = avg(statistics, attempt) #calculate average number
	print("===================================================")
	print("Tried {} times on average for each hash value.".format(avg_time))
