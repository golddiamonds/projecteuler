#A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
#If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
#The lexicographic permutations of 0, 1 and 2 are:

#012   021   102   120   201   210

#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9

#strategy
#		going to use permutations

import math

permutations = []
for i in range(0,10):
	permutations.append(math.factorial(i)) #9 spaces after 1st space

def number_of_perms(i, total_left, permutations = permutations):
	total = 0
	numbers = 0
	while total < total_left:
		total += permutations[i]
		numbers += 1
	total -= permutations[i]
	numbers -= 1
	total_left -= total
	return [numbers,total_left]

#how many first numbers can you go through and stay below 1M? (i.e. total_left)

output = [0,1000000]
num_output = []
for i in range(0,9):
	output = number_of_perms((9-i),output[1])
	#print i, output[0] + 1
	num_output.append(output[0])

numbers = [0,1,2,3,4,5,6,7,8,9]
for i in num_output:
	#print i
	print numbers[i]
	numbers.remove(numbers[i])

#and then print last remaining number
print numbers[0]