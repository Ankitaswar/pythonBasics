
def BubbleSort(lst):

    for i in range(len(lst)-1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                #swap
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp

lst = [5,3,8,6,7,2]
BubbleSort(lst)
print(lst)
