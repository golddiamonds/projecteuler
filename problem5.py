#problem5

#Q: What is the smallest positive number that is evenly divisible by all th enumbers from 1 to 20?

#Implementation:
#		- begin at 20 (must be divisible by 20)
#		- check modulo
#		- upper limit of 20!



class SmallestMultiple:
	def __init__(self, min, max):
		self.min = min
		self.max = max
		self.n = 1
		self.factorial()

	#upper bounds on smallest multiple
	def factorial(self):
		for i in range(self.min, self.max+1):
			self.n = self.n * i

	#start with max and go lower
	def check_lower(self):
		start = 20
		while start < self.n:
			for i in range(self.min+1, self.max+1):
				#print i
				if (start % i) != 0:
					break
				if (i == self.max):
					print 'success for: ', start
					start = self.n
			start += 20
			#print start

if __name__ == '__main__':
	small = SmallestMultiple(1,20)
	small.check_lower()

