#problem 67

#import text file triange into script
#use logic developed in problem 18
#profit!

f = open('problem67_triangle.txt')

rows = []
for line in f:
	rows.append(line.rsplit(' '))

for j in range(1, len(rows)):
	for i in range(0, len(rows[len(rows) - j])-1):
		k = (len(rows) - j)
		if int(rows[k][i]) >= int(rows[k][i+1]):
			rows[k-1][i] = int(rows[k-1][i]) + int(rows[k][i])
		else:
			rows[k-1][i] = int(rows[k-1][i]) + int(rows[k][i+1])

print rows[0]