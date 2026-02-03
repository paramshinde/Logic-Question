#Print all prime numbers between 1 and 100.
num=1
while num<101:
    count=0
    i=1
    while i<=num:
        if num%i==0:
            count=count+1
        i=i+1
    if count==2:
        print(num,"Prime")
    num=num+1