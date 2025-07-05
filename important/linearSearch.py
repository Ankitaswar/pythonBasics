pos = -1
def linearSearch(lst, n):

    for i in lst:
        globals()['pos'] += 1
        if i == n:
            return True

    return False

lst = [1,2,3,4,5,6,10]

if linearSearch(lst, 4):
    print("found at pos", pos+1)
else:
    print('Not Cound', pos+1)