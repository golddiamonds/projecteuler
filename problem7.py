#problem7

#Q: what is the 10,001st prime number?

#Implementation
#		start with 13 (the 6th prime)
#		add 2
#		check for primality beginning with 3 and moving up
#		if prime add to prime count, move on (add 2)
#		if not prime, move on (add 2)
#		if prime count == 10,001 then that number is the prime you want!

from math import sqrt, ceil

class PrimeCount:
	def __init__(self, pnum):
		self.pnum = pnum
		self.prime_count = 6
		self.n = 15

	def main(self):
		while self.prime_count < self.pnum:
			for i in range(3, int(sqrt(self.n)) + 1):
				if self.n % i == 0:
					break
				if i == int(sqrt(self.n)):
					self.prime_count += 1
					print 'prime: ', self.n
					print 'primecount: ', self.prime_count
			self.n += 2

if __name__ == '__main__':

	prob7 = PrimeCount(10001)
	prob7.main()