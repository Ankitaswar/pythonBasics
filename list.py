nums = [25, 12, 35, 39.0]  #mutable
print(nums)
print(nums[0])
print(nums[-1])

names = ['Ankit', 'Aswar']
print(names)

values = [9.5, "Ankit", 12]
print(values)

mil = [nums, names]
print(mil)

nums.append(88)  # add at the end
nums.insert(1, 90)  # in btw
print(nums)

nums.remove(12)  #based on element
remElement = nums.pop(0) #based on index--> return ele
print(remElement)
print(nums)

nums.pop()  # remove last element

del nums[2:]  #delete multiple values
print(nums)

nums.extend([23,55,62])  #insert multiple value
print(nums)

print(min(nums))
print(sum(nums))

nums.sort()
print(nums)

