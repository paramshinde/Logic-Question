#Check whether the given number is an Armstrong number.
num=153
res=1
arm=0
dup=num
count=len(str(num))
while num>0:
    res=(num%10)**count
    arm=arm+(res)
    num=num//10
if dup==arm:
    print("Amstrong")
else:
    print("Error")