nums = [1,2,3,4,5]

it = iter(nums)
print(it.__next__())
#OR
print(next(it))

for i in nums:
    print(i)

print("----------------")

#create our own iterator
class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <=10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

values = TopTen()

print(next(values)) #this will print 1 now for loop will start from 2

for i in values:
    print(i)