#problem 12

#Q: what is the value of the first triangle number to have over five hundred divisors?

#Implmentation
#		lets try a simple naive implementation

tri_num = 17907120
hi_count = 0
for i in range(5985,100000):
	#print i
	tri_num = tri_num + i
	#print tri_num
	div_count = 0
	#print 'tri num', tri_num
	#find divisors
	divisors = []
	for k in range(1, tri_num +1):
		if (tri_num % k) == 0:
			#print k
			divisors.append(k)
			#print div_count
	#print divisors
	if len(divisors) > 500:
		print 'FOUND IT', tri_num, ' with ', hi_count, ' @ ', i
		break
	#print len(divisors)
	if len(divisors) > hi_count:
		hi_count = len(divisors)
		print 'hi!', tri_num, ' with ', hi_count, ' @ ', i

print 'gotta try higher'