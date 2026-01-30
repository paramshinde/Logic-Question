#Find and print the sum of digits of the given number
num=123
res=1
while num>0:
    res=res*num%10
    num=num//10
print(res)