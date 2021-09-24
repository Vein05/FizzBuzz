#This is my second try over the famous FizzBuzz problem



for i in range(1, 101):

	if ( i % 3 == 0 ) and ( i % 5 == 0):
		print("FizzBuzz")
		continue
		

	else:
		if (i % 3 == 0):
			print("Fizz")

		elif (i % 5 == 0):
			print("Buzz")
		
		else:
			print(i)
		

