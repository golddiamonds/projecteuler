#problem 3 on projecteuler.com

#Q: what is the largest prime factor of the number 600851475143

#Implementation:
#		we should probably take the sqrt of the number first
#			- no need to go above this value
#		then find factors
#		then do something similar to filter out non-primes

from math import sqrt

val = 600851475143
sqrt_val = int(sqrt(val))

factors = []
while sqrt_val > 0:
	if (val % sqrt_val) == 0:
		factors.append(sqrt_val)
	sqrt_val -= 1

print factors

for factor in factors:
	print factor
	sqrt_val = int(sqrt(factor))
	while (sqrt_val > 0):
		if (factor % sqrt_val) == 0:
			print str(sqrt_val) + ',' + str(factor)
		sqrt_val -= 1

print factors