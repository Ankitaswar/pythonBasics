names = ["Navin", "Ankit", "Vikas"]
comps = ["Dell", "Mac", "Lenevo"]

zipped = list(zip(names, comps))  #set, dict
print(zipped)

zippe = zip(names, comps)
for a,b in zippe:
    print(a,b)