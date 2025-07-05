# nums = [12, 15, 18, 21, 26, 25]
nums = [12, 18, 21, 26]

for num in nums:
    if num % 5 ==0:
        print(num)
        break
else:
    print("Not Found")