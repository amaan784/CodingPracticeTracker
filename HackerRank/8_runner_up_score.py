if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    """
    # First method - shorter, more pythonic way
    arr_list = list(arr)
    print(list(set(sorted(arr_list)))[-2])
    """

    # Second method - 
    # convert map object to list
    l = list(arr)
    
    # get the maximum value of the list
    maxVal = max(l)
    
    # remove all occurences of the maxvalue
    while True:
        if maxVal not in l:
            break
        else:
            l.remove(maxVal)
    
    # the max value of the current list will be the runner up of the old list
    secondMaxVal = max(l)
    print(secondMaxVal)
    