#Print all prime numbers between 1 and 100.
num=1
while num<101:
    print(num)
    count=0
    i=1
    while num>=i:
        if num%i==0:
            count=count+1
        i=i+1
        if count<2:
            print(i,"Prime")
        else:
            print("Not") 
    num=num+1