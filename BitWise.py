#Complement(~), And(&), Or(|), XOR(^), Left Shift(<<), Right Shift(>>)

print(~12)  # -13
# 00001100 ==> Compl => 11110011
# why negative --> 2's compliment = 1's Compl + 1
# 13 => 00001101 -> 1's compl -> 11110010  + 1 ==> 11110011 (-13)(2's Compl of 13 which is -13)

print(12 & 13)  # 12
# 00001100 (12)
# 00001101 (13)
# 00001100  => 12

print(12 | 13)  # 13
# 00001100 (12)
# 00001101 (13)
# 000011001 => 13

#XOR -> both the number are diff then will get 1 and if same will get 0
print(12 ^ 13)  # 1
# 00001100 (12)
# 00001101 (13)
# 000000001 => 1

#Left Shift <<
print(10 <<2)  # 40
# 00001010 -> 00101000 (40)

#right Shift >>
print(10 >>2)  # 2
# 00001010 -> 00000010 (2)
