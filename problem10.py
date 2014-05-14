#problem 10

#Q: find the sum of all primes below two million

#implentation:
#		find primes below 2M
#		only look at odds
#		only look at <= ceil(sqrt(n))

from math import ceil, sqrt

primes = [2,3,5]

for n in range(7,2000000): #2000000):
	#print n
	#print int(ceil(sqrt(n)) + 1)
	for j in range(2,int(ceil(sqrt(n))) + 1):
		#print j
		if (n % j) == 0:
			#print j, n, 'not prime!'
			break
		if j == int(ceil(sqrt(n))):
			print 'prime! ', n
			primes.append(n)

#print primes

prime_sum = 0
for i in primes:
	prime_sum += i

print prime_sum