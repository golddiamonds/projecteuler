#problem6

#Q: find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

class SumSquareDifference:
	def __init__(self, n):
		self.n = n

	def calcSumOfSquares(self):
		sos = 0
		for i in range(1, self.n + 1):
			sos += i*i
		return sos

	def calcSquareOfSum(self):
		sos = 0
		for i in range(1, self.n + 1):
			sos += i
		return sos*sos


if __name__ == '__main__':

	prob6 = SumSquareDifference(100)
	sos1 = prob6.calcSumOfSquares()
	sos2 = prob6.calcSquareOfSum()
	print 'answer: ', sos2 - sos1