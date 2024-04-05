'''
My answer to 1.3.
'''
def minmax(data=[]):  #  This function returns the minimum and maximum values
    if data == []:    #  of a list sequence in a tuple without using built-in
        return None   #  min() and max() functions
    else:
        data.sort()    #  Sorting the values in ascending order
        min = data[0]  #  The minimum value
        max = data[-1] #  The maximum value
        return (min, max)
    

if __name__ == '__main__':
    print(minmax([2, 5, 8, 4]))
    print(minmax())
    print(minmax([2, 1]))
    print(minmax([5]))