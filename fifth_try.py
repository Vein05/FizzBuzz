#This is something i looked up online lol

for i in range(1, 101):
	r = ""
	if (i % 3 == 0 ):
		r += "Fizz"

	if (i % 5 == 0):
		r += "Buzz"

	print( r or i)