
def fizzbuzz(input_integer):
	if input_integer % 15 == 0:
		return "fizzbuzz"
	elif input_integer % 3 == 0:
		return "fizz"
	elif input_integer % 5 == 0:
		return "buzz"
	else:
		return input_integer

