# My last try over this problem and the most interactive one? Not sure lol


import time


start = int(input("Enter the number for the code to start from : "))
end = 1 + int(input("Enter the number for the code to end at : "))

fizz = int(input("Enter the number that's going to be Fizz : "))
buzz = int(input("Enter the number that's going to be Buzz : "))

start_time = time.time()

fizbuz_list = [
	(fizz, "Fizz"),
	(buzz, "Buzz")
]

for i in range(start, end):
	
	r = ""
	for v in fizbuz_list:
		if ( i % v[0] == 0):
			r += v[1]
	if r:
		print(r)
	else:
		print(i)


print("It took %s seconds to complete this bullshit!" % (time.time() - start_time))