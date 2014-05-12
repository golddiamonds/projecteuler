#problem 14

#Q: find the longest Collatz chain starting with a number under 1,000,000

max_start = 1000000
longest_count = 0
chain = 0
longest_num = 0

for i in range(1,1000000):
	num = i
	count = 0
	if (i % 1000) == 0:
		print i
	while num > 1: 
		if (num % 2) == 0:
			num = num/2
			count += 1
		else:
			num = (3*num + 1)
			count += 1
	if count >= longest_count:
		longest_count = count
		longest_num = i
		print count
		print i, 'is >='

print longest_num, longest_count
