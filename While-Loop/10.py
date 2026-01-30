#Find and print the product of all digits of a given number.
num=512
res=0
while num>0:
    res=res+num%10
    num=num//10
print(res)