'''
My answer to 1.5.
'''
def sum_of_squared_integers(number):
    return sum([integer ** 2 for integer in range(number)])  #  Uses list comprehension and the sum() function to achieve the same results as 1-5.py


if __name__ == '__main__':
    print(sum_of_squared_integers(5))
    print(sum_of_squared_integers(11))