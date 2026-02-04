#Find the LCM (Least Common Multiple) of two given numbers.
a=10
b=30
limit=max(a,b)
total=a*b
LCM=0
while limit<=total:
    if limit%a==0 and limit%b==0:
        LCM=limit
        break
    limit=limit+1
print(LCM)