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


def compareAll(lhash, data, total, unit_length, tlen):
	#(lhash) contains multiple history entries appended at the end without any overhead
	#(data) is the current entry you are comparing with the (lhash) items
	#(total) is the length of (lhash)
	#(unit_len) is the length of each entry
	#(tlen) is the length (tlen/2 bytes) you are comparing between (lhash)'s entries and (data)

	index = 0
	while index < tlen:
		flag = compare(data, lhash[index])
		if flag == 1: #if not the same
			break
		else:
			return index

	return -1 #no match, return -1


if __name__ == '__main__':
	if len(sys.argv) < 2:
		pring("Usage: cfb AttemptCount")
		sys.exit(1)

	attempt = int(sys.argv[1])
	count = 0
	statistics = []
	hashHistory = []

	while count < attempt:
		data = os.urandom(16)
		dataBackup = data

		c = 0 #store how many attemps has done for one specific hash value

		h = MD5.new()
		index = -1
		while index < 0: #keep looping until there is a collision
			if c > 0:
				hashHistory.append(data_hash) #not match, so store the previous result

			h.update(data)
			data_hash = h.hexdigest()
			index = compareAll(hashHistory, data_hash, c, 32, 6)
			data = add(data)
			c += 1

		for j in range(0, index):
			dataBackup = add(dataBackup) #reconstruct the history message
		print("* Hash value Match: tried for {} times".format(c))
		print("  Message one:   "),
		display(dataBackup, 0, 16)
		print("\n"),
		print("  Message two:   "),
		display(data, 0, 16)
		print("\n"),
		print("   Hash Value:   "), 
		print(data_hash[0:2] + " " + data_hash[2:4] + " " + data_hash[4:6])
		statistics.append(c)
		count += 1

	avg_time = avg(statistics, attempt) #calculate average number
	print("===================================================")
	print("Tried {} times on average for each hash value.".format(avg_time))
