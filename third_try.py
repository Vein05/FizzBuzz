#This is my third try over the famous FizzBuzz problem



for i in range(1, 101):

	result = ""

	if (i % 3 == 0):
		result += "Fizz"

	elif (i % 5 == 0):
		result += "Buzz"

	else:
		result += str(i)

	print(result)