#problem 19

#1 Jan 1900 was a Monday
#30 days in Sept (9), Apr (4), June (6), Nov (11)
#31 in rest of months (1,3,5,7,8,10,12)
#28 in Feb (2), except on leap years when it has 29
#		if year % 4 == 0 then a leap year, except on a century unless divisible by 400 (century % 400 == 0).

#Q: how many sundays fell on the first of the month during the twentieth century (1 jan 1901 to 31 dec 2000)?

class Months:
	def __init__(self):
		self.months = {1:31,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
	def returnCount(self,month_int,year=None):
		if month_int != 2:
			return self.months[month_int]
		if year % 100 == 0:
			#then a century
			if year%400 == 0:
				return 29
			return 28
		if year % 4 == 0:
			return 29
		return 28

if __name__ == '__main__':

	month_test = Months()

	#count days for every month
	days = 0
	sundays = 0
	first_of_month = 0
	for i in range(1900,2001):
		for j in range(1, 13):
			print i, j, ':', month_test.returnCount(j,i)
			days += month_test.returnCount(j,i)
			print days
			first_of_month = days + 1
			print first_of_month
			if (first_of_month % 7 == 0) and (i > 1900):
				print 'a sunday past 1901'
				sundays += 1

	print days
	print sundays