
def count(list):
    even = 0
    odd = 0

    for i in list:
        if i%2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


lst = [12,176,87,38,95,847,30]
even, odd = count(lst)
print("Even : {} and odd: {}".format(even, odd))

