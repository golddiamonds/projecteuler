#problem9

#Q: find the product abc of the pythagorean triple for which a + b + c = 1000

#implementation:

class PythagoreanTriples:
	def __init__(self, maxprod=1000):
		self.maxprod = maxprod
		self.a = 3
		self.b = 4
		self.c = 5

	def checkTriple(self, a, b, c):
		if ((a*a) + (b*b) == (c*c)):
			return True
		return False

	
