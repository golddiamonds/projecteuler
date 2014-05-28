#problem22

f = open('problem22_names.txt')

#put names into a list
for line in f:
	names = line.rsplit('","')

#strip quote on first and last name
names[0] = names[0][1:]
names[len(names)-1] = names[len(names)-1][:-1]

#sort list
names.sort()

i = 1
total = 0
#alphabet for calculating values using find()
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#run through list of names; calculate values and total
for name in names:
	value = 0
	for letter in name:
		letter_value = int(letters.find(letter)) + 1
		value += letter_value
	value *= i
	total += value
	i += 1
print total
