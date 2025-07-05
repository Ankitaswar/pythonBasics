#Similar to list but tuple is immutable

tup = (21,34,56,78,21)

# tup[1] = 33 # throw error can't change

print(tup)
print(tup.count(21))  # count value iteration
#as we don't change the tuple so iteration is faster than the list