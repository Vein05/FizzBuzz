
#This is my fourth try over the famous FizzBuzz problem


def c(n):
	
	if (n % 3 ==0 ) and (n % 5 == 0):
		return "FizzBuzz"

	else:

		if (n % 3 == 0):
			return "Fizz"

		elif (n % 5 == 0):
			return "Buzz"

		else:
			return n



for i in range(1, 101):
	print(c(i))