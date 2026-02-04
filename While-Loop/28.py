num=923
small=9
while num>0:
    digit=num%10
    if digit<small:
        small=digit
    num=num//10
print(small)