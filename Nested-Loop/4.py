#Print all prime numbers up to n using nested loop checking.
num=10
for i in range(1,num+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count=count+1
    if count==2 or i==1:
        print(i,"Prime")
    else:
        print(i,"Not")