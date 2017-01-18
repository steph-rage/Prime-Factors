def prime_factors(number):
	factors = []				#Initialize the list of factors
	def find_factors(n):
		max_check = max(int(n**0.5), 2)
		test = 0
		for i in range(2, max_check+1):
			if n%i == 0:
				factors.append(i)
				test = 1
				if n != i:
					find_factors(int(n/i))
				break
		if test == 0:
			factors.append(n)
	find_factors(number)
	return(factors)

thing = float(input("Pick a positive integer: "))
if int(thing) == thing and thing >= 1:
	print(prime_factors(int(thing)))
else:
	print("That is not a positive integer; please try again")


