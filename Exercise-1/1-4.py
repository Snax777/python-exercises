'''
My answer to 1.4.
'''
def sum_of_squared_integers(number):
    sum = 0

    for integer in range(number):
        sum += integer ** 2

    return sum  #  Returns the sum of of the squares of all positive integers smaller than the given number


if __name__ == '__main__':
    print(sum_of_squared_integers(5))
    print(sum_of_squared_integers(11))