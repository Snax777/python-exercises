'''
My answer to 1.7.
'''
def sum_of_squared_odd_integers(number):                           #  Using list comprehension,respectively setting range function's 'start', 'end' and 'step' parameter to
    return sum([integer ** 2 for integer in range(1, number, 2)])  #  1, value of 'number' parameter and 2, and the sum() function to achieve the smae results as 1-6.py


if __name__ == '__main__':
    print(sum_of_squared_odd_integers(10))
    print(sum_of_squared_odd_integers(4))
    print(sum_of_squared_odd_integers(5))