
## problem 1 on projecteuler.com

## Q: find the sum of all multiples of 3 or 5 below 1000.

## simple implementation:
## 		place all multiples of 3 (<1000) into a list
##		place all multiples of 5 (<1000) into a list
##		remove duplicates
##		take the sum of both lists.


#multiples of 3
mult_of_three = []
for i in range(3,1000,3):
	mult_of_three.append(i)

#multiples of 5
mult_of_five = []
for i in range(5,1000,5):
	mult_of_five.append(i)

#remove duplicates
for i in mult_of_five:
	if i in mult_of_three:
		mult_of_three.remove(i)

#now take sums
sum_three = sum(mult_of_three)
sum_five = sum(mult_of_five)

#sum of both
both = sum_three + sum_five

#answer
print both