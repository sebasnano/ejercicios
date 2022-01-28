import random
import time


def naiveSearch(list, object):
    for i in range(len(list)):
        if list[i] == object:
            return i
    return -1


def binarySearch(list, object, high=None, low=None):
    if low is None:
        low = 0
    if high is None:
        high = len(list) - 1
    if high < low:
        return -1
    mid = (low + high) // 2
    if list[mid] == object:
        return mid
    elif list[mid] < object:
        return binarySearch(list, object, low=low, high=mid - 1)
    else:
        return binarySearch(list, object, low=mid + 1, high=high)

if __name__=='__main__':
    size = 1000
    init = set()
    
    while len(init) < size:
        init.add(random.randint(-3*size, 3*size))
        
    listTidy = sorted(list(init))
    
    start = time.time()
    for object in listTidy:
        naiveSearch(listTidy, object)
    end = time.time()
    print(f'Naive Search: {end - start} seconds')
    
    start = time.time()
    for object in listTidy:
        binarySearch(listTidy, object)
    end = time.time()
    print(f'Binary Search: {end - start} seconds')
        