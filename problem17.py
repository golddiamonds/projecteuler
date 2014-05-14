#problem 17


number_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
				9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
				16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty'} 

number_dict_tens = {2:'twenty', 3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}

number_str = ''
for n in range(1, 21):
	number_str += number_dict[n]

for n in range(21,100):
	#print str(n)
	#print str(n)[0]
	if str(n)[1] != str(0):
		number_str += number_dict_tens[int(str(n)[0])] + number_dict[int(str(n)[1])]
	else:
		number_str += number_dict_tens[int(str(n)[0])]

for n in range(100,1000): #don't forget 1,000 later!
	#print n
	if (str(n)[1] == '0' and str(n)[2] == '0'):
		#print number_dict[int(str(n)[0])] + 'hundred'
		number_str += number_dict[int(str(n)[0])] + 'hundred'
	elif (int(str(n)[1]) == 1):
		#print number_dict[int(str(n)[0])] + 'hundred' + 'and' + number_dict[int((str(n)[1] + str(n)[2]))]
		number_str += number_dict[int(str(n)[0])] + 'hundred' + 'and' + number_dict[int((str(n)[1] + str(n)[2]))]
	elif (int(str(n)[1]) == 0):
		#print number_dict[int(str(n)[0])] + 'hundred' + 'and' + number_dict[int((str(n)[1] + str(n)[2]))]
		number_str += number_dict[int(str(n)[0])] + 'hundred' + 'and' + number_dict[int((str(n)[1] + str(n)[2]))]
	elif (int(str(n)[1] + str(n)[2]) <= 20):
		#print number_dict[int(str(n)[0])] + 'hundred' + 'and' + number_dict[int((str(n)[1] + str(n)[2]))]
		number_str += number_dict[int(str(n)[0])] + 'hundred' + 'and' + number_dict[int((str(n)[1] + str(n)[2]))]
	else:
		#print number_dict[int(str(n)[0])] + 'hundred' + 'and',
		number_str += number_dict[int(str(n)[0])] + 'hundred' + 'and'
		if str(n)[2] != str(0):
			#print number_dict_tens[int(str(n)[1])] + number_dict[int(str(n)[2])]
			number_str += number_dict_tens[int(str(n)[1])] + number_dict[int(str(n)[2])]
		else:
			#print number_dict_tens[int(str(n)[1])]
			number_str += number_dict_tens[int(str(n)[1])]

#print 'onethousand'
number_str += 'onethousand'
		

#print number_str
print len(number_str)