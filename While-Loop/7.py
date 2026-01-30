#Calculate the sum of all even numbers from 1 up to n.
n=int(input("enter NO:"))
i=1
res=0
while i<=n:
    if i%2==0:
        res=res+i
    i=i+1
print(res)