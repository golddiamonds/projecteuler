#sieve of erathosthenes
#or: collecting prime numbers...

#basic idea:
#1. generate list of integers to test for primality
#2. start with lowest, exclude all multiples of that number from list
#3. continue until this has been done with all integers on list.
#4. you now have a list of primes...

class Sieve:
	def __init__(self, max):
		#largest integer to test
		self.max_integer = max
		#list of integers to test
		self.integer_list = []
		self.createList()
		self.primality()

	def createList(self):
		for i in range(2, self.max_integer+1):
			self.integer_list.append(i)

	def primality(self):
		i = 2
		while i <= self.max_integer:
			#remove all multiples of i
			j=i+i
			while j <= self.max_integer:
				if j in self.integer_list:
					self.integer_list.remove(j)
				j+=i
			i+=1

if __name__ == '__main__':
	prime_list = Sieve(28123)
	print prime_list.integer_list