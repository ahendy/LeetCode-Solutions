
def count_and_say(n):
	word = "1"
	for i in range(1, n):
		count, temp = 1, ""
		for j in range(1, len(word)+1):
			if j == len(word) or word[j] != word[j-1]:
				temp += "".join([str(count), word[j-1]])
				count = 1
			else:
				count += 1

		word = temp
	
	return word

if __name__ == '__main__':
	
	tests = (
		(2, '11'),
		(3, '21'),
		(4, '1211'),
		(5, '111221'),
		(6, '312211'),
	)
	
	for i, (param, sol) in enumerate(tests):
		assert count_and_say(param) == sol
		print "Passed test %d." % (i, )