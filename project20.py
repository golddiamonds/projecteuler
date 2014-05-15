#problem 20

#Q: find the sum of the digits in the number 100!

from math import factorial

sum = 0
for num in str(factorial(100)):
	sum += int(num)
print sum