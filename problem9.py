#problem9

#Q: find the product abc of the pythagorean triple for which a + b + c = 1000

#implementation:
#		lets find the triplet first

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

#generate list of lists of potential triplets
#a < b < c
#a + b + c = 1000

triplets = []
for a in range(1,1000):
	for b in range(2, 1000):
		for c in range(3, 1000):
			if (c > b) and (b > a) and ((a*a) + (b*b) == (c*c)):
				print a,b,c, a+b+c
				if (a + b + c) == 1000:
					print 'FOUND!'
				#triplets.append([a,b,c])

#print triplets
#pythag = PythagoreanTriples()

#print pythag.checkTriple(3,4,5)
