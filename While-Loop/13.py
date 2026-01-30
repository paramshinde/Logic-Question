#Check whether the given number is a palindrome.
num=122
dup=num
res=0
while num>0:
    res=res*10+num%10
    num=num//10
if dup==res:
    print("Palindrome")
else:
    print("Not Palindrome")