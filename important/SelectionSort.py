# find min or max value at put the correct pos

def SelectionSort(lst):
    for i in range(len(lst)-1):
        minPos = i
        for j in range(i, len(lst)):
            if lst[j] < lst[minPos]:
                minPos = j

        temp = lst[i]
        lst[i] = lst[minPos]
        lst[minPos] = temp



lst = [5,3,8,6,7,2]
SelectionSort(lst)
print(lst)
