'''
My answer to 1.6.
'''
def sum_of_squared_odd_integers(number):
    sum = 0

    for integer in range(number):
        if integer % 2 == 1:     #  Checks for any odd integers, then proceeds
            sum += integer ** 2  #  to square them individually and add them together

    return sum


if __name__ == '__main__':
    print(sum_of_squared_odd_integers(10))
    print(sum_of_squared_odd_integers(4))
    print(sum_of_squared_odd_integers(5))