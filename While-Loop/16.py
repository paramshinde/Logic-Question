#Check whether the given number is a Perfect number
num=28
og=num
i=1
res=0
while num>i:
    if num%i==0 and og!=i:
        res=res+i
    i=i+1
if num==res:
    print("Perfect Number")
else:
    print("Error")