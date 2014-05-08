#problem 4

#Q: find the largest palindrome made from the product of two 3-digit numbers

#Implementation:
#		start with the largest 3-digit numbers then drop from there (e.g. 999x999, 999x998)


import math

class Palindrome:
	def __init__(self):
		pass

	def calculate_range(self, n):
		vals = []
		for i in range(1,n+1):
			vals.append(i * n)
		return vals

	def check_palindrome(self, n):
		length_n = len(n)
		if (length_n % 2) == 0:
			for i in range(0, length_n/2):
				if n[i] != n[length_n-(i+1)]:
					break
				if int(i) == int(length_n/2 - 1):
					return True
			return False
		elif (length_n % 3) == 0:
			for i in range(0, int(math.floor(length_n/2) - 1)):
				if n[i] != n[length_n - (i+1)]:
					break
				if int(i) == int(math.floor(length_n/2)):
					return True
			return False

	def main(self, min, max):
		vals = []
		palindromes = []
		for i in reversed(range(min, max+1)):
			vals.append(self.calculate_range(i))
			#print i
		#print vals
		for num_set in vals:
			for num in num_set:
				if self.check_palindrome(str(num)):
					#print 'palindrome: ', num, '\n'
					palindromes.append(num)
					break
		maxpal = 0
		for palindrome in palindromes:
			if int(palindrome) > int(maxpal):
				maxpal = palindrome
		print 'max: ', maxpal

if __name__ == '__main__':
	pal = Palindrome()
	pal.main(500,1000)



