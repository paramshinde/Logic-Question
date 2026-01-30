#Reverse the given number and print the reversed value
num=123
res=0
while num>0:
    res=res*10+num%10
    num=num//10

print(res)