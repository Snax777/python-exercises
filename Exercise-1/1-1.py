'''
My answer to 1.1.
'''
def is_multiple(multiple, integer):  #  This function uses the modulo operator to check
    return integer % multiple == 0   #  if the 'multiple' value is a multiple of the 'integer' value


if __name__ == '__main__':
    print(is_multiple(4, 12))
    print(is_multiple(5, 31))