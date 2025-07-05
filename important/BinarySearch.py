#sorted value
pos = -1

def BinarySearch(lst, n):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid =(high+low)//2
        if lst[mid] == n:
            globals()['pos'] = mid
            return True
        elif lst[mid] > n:
            high = mid - 1
        else:
            low = mid + 1
    return False

lst = [4,9,13,23,49,97]
if BinarySearch(lst, 33):
    print("Found at ",pos)
else:
    print("Not Found")