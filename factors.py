

def prime_factors(number):
    prime_digits = []

    if not isinstance(number, int):
        raise ValueError("Number must be an integer")
    
    if number / number == 1 and number / 1 == number and number % 2 != 0 and number % 3 != 0:
        prime_digits.append(number)
    else:

        while number % 2 == 0:
            prime_digits.append(2)
            number /= 2

    




    return prime_digits
    



