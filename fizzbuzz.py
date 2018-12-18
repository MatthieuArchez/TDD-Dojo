"""
	FIZBUZZ module
"""

def fizzbuzz(input_integer):
    """
        return fizz     when modulo 3
               buzz     when modulo 5
               fizzbuzz when modulo 15
    """
    if input_integer % 15 == 0:
        return "fizzbuzz"
    elif input_integer % 3 == 0:
        return "fizz"
    elif input_integer % 5 == 0:
        return "buzz"

    return input_integer
