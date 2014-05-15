#problem 25

#Q: What is the first term in the Fibonacci sequence to contain 100 digits?

def fibonacci(n_1,n_2):
	n = n_1 + n_2
	return n

fib = ''
n_1 = 1
n_2 = 1
n = 2
while len(fib) < 1000:
	fib = str(fibonacci(int(n_1), int(n_2)))
	n_2 = int(n_1)
	n_1 = (int(fib))
	n += 1

#print fib
print n