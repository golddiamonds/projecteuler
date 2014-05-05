##problem 2 on projecteuler.com

##Q: Find the sum of the even-valued Fibonacci terms that do not exceed four million.

##Implementation:
##		Calculate all Fibonacci terms below four million
##		Place into list
##		Get even terms
##		Take sum of list


class Fibonacci:
	def __init__(self, n=False):
		self.max_n = n
		self.values = [1,1]
		if self.max_n:
			while (self.values[-1] < n):
				self.calculate_next()
			self.values = self.values[:-1]
			#print self.values

	def calculate_next(self):
		next = (self.values[-2] + self.values [-1])
		self.values.append(next)

	def get_even(self):
		even = []
		for term in self.values:
			if (term % 2) == 0:
				even.append(term)
		return even


if __name__ == '__main__':
	fib = Fibonacci(4000000)
	even = fib.get_even()
	print sum(even)

