#sieve of erathosthenes
#or: collecting prime numbers...

#basic idea:
#1. generate list of integers to test for primality
#2. start with lowest, exclude all multiples of that number from list
#3. continue until this has been done with all integers on list.
#4. you now have a list of primes...

#largest integer to test
max_integer = 28123

#create list of integers to test
integer_list = []
for i in range(2, max_integer+1):
	integer_list.append(i)

i = 2
while i <= max_integer:
	#remove all multiples of i
	j=i+i
	while j <= max_integer:
		if j in integer_list:
			integer_list.remove(j)
		j+=i
	i+=1

#print out the remaining list
#these will be all primes
print integer_list