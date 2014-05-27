#problem 18

#Q: starting at the top and moving to adjacent numbers below, find the max sum of these numbers in the triangle provided

# if array index = 0 then can access same array index below or index + 1
# if array index != 0 then can access array index below or index +/- 1

#implemtnation:

#			1) start at second to last row
#			2) compare to last row below, and last row below + 1.
#					a) choose largest of two. add to value in second to last row.
#					b) overwrite value in second to last row.
#			3) move up one row and do again.


rows = [[75]
,[95, 64]
,[17, 47, 82]
,[18, 35, 87, 10]
,[20, 4, 82, 47, 65]
,[19, 1, 23, 75, 3, 34]
,[88, 2, 77, 73, 7, 63, 67]
,[99, 65, 4, 28, 6, 16, 70, 92]
,[41, 41, 26, 56, 83, 40, 80, 70, 33]
,[41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
,[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
,[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
,[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
,[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
,[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]


for j in range(1, len(rows)):
	for i in range(0, len(rows[len(rows) - j])-1):
		k = (len(rows) - j)
		if rows[k][i] >= rows[k][i+1]:
			rows[k-1][i] += rows[k][i]
		else:
			rows[k-1][i] += rows[k][i+1]

print rows[0]