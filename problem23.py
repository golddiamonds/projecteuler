#problem23


# 1. find all abundant numbers <= 28123
# 2. create list of all dual-sums of those numbers <= 28123
# 3. create list with numbers not on this list
# 4. sum them
# 5. profit

#1a. Abundant numbers cannot be prime, obviously (1 will not be > p).
#	-- use sieve to generate list of primes <= 28123. remove those from abundant number list

from extras import sieve
import math

#list to be pared down to include abundant numbers only
abundant_numbers = []
#add all numbers > 1 and <=28123
for i in range(2,28124):
	abundant_numbers.append(i)

#generate primes
primes = sieve.Sieve(28123)
for i in primes.integer_list:
	if i in abundant_numbers:
		abundant_numbers.remove(i)


#find divisors of all numbers in list (use modificaiton of problem21's find_divisors() function)
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
	return divisors

divisor_dict = {}
#finding divisors
abundant_numbers_found = []
for i in abundant_numbers:
	if i < sum(find_divisors(i)):
		abundant_numbers_found.append(i)

#should now have abudundant numbers!
#print abundant_numbers_found

#now create list of integers formed by pairs of these numbers:
an_sum_list = []
for i in abundant_numbers_found:
	an_sum_list.append(i+i)
	for j in abundant_numbers_found:
		if j > i:
			if (j+i) < 28124:
				an_sum_list.append(j+i)

#print an_sum_list

all_numbers = []
for i in range(1,28124):
	all_numbers.append(i)

for i in an_sum_list:
	if i in all_numbers:
		all_numbers.remove(i)
		print 'removing', i

print all_numbers
print sum(all_numbers)