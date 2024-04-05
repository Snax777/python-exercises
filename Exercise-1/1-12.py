from random import randrange


'''
My answer to 1.12.
'''
def choice(data):
    if isinstance(data, int):
        return randrange(data)
    else:
        if len(data) > 0:
            return data[randrange(len(data))]
        

if __name__ == '__main__':
    print(choice(9))
    print(choice([1, 4, 6, 7, -3, -12]))
    print(choice((4, 6, 2, 5, -1)))