# iterator we need to define next and iter by our own but now generator will do this

def topten():
    yield 1
    yield 3
    yield 5

values = topten()
print(values) #generator
print(values.__next__())
print(values.__next__())

def TopTenGen():
    n= 1

    while n <=10:
        sq = n*n
        yield sq
        n += 1

sqrs = TopTenGen()

for i in sqrs:
    print(i)

#useCase: we are fetching thousand of data from db all these thousand recorded loaded in your memory we don't\
# want that what is work with one value at a time.

