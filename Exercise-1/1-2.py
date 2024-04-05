'''
My answer to 1.2.
'''
def is_even(number): #  Checks if the given value is even without
    value = number   #  using either the division or modulus operator

    while value > 1: 
        value -= 2

    return value == 0 # returns True if there is no remainder -- it is even(value = 0)


if __name__ == '__main__':
    print(is_even(12))
    print(is_even(31))