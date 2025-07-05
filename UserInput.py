x = int(input("Enter Value 1" ))  #Always return string
y = int(input("Enter Value 2" ))  #Always return string
z = x + y
print(z)

ch = input("Enter char")[0]
print(ch)

res = eval(input("Enter Expression: "))  # 2 + 3 -7
print(res)

# run file from cli passing some para -> EX :  python3 mycode.py 3  5
#    Index                                                0      1  2
import sys
x = int(sys.argv[1]) # 3
y = int(sys.argv[2]) # 5