#problem 21

#find the proper divisors
#only need to find divisors up to sqrt(n), then find opposites

import math

sum_divs = {}

def find_divisors(n):
	i = 2
	divisors = []
	#find first half
	while i <= math.sqrt(n):
		if n % i == 0:
			divisors.append(i)
		i += 1
	for i in divisors:
		divisor_2 = n/i
		if divisor_2 not in divisors:
			divisors.append(divisor_2) 
	#all have 1 as a divisor
	divisors.append(1)
	sum_divs[n] = sum(divisors)

for i in range(1,10000):
	find_divisors(i)

#find amicable

#print sum_divs

amicable = []
for i in sum_divs:
	j = i + 1
	#print i
	while j < 10000:
		if (int(i) == int(sum_divs[j])) and (int(j) == int(sum_divs[i])):
			amicable.append(i)
			amicable.append(j)
			print i, j
		j+=1

print sum(amicable)