#problem 16

#Q: 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26
#What is the sum of the digits of the number 2^1000

#implementation:
#let's do this the naive way


number = str((pow(2,1000)))

sum_of_digits = 0
for i in number:
	sum_of_digits += int(i)

print sum_of_digits