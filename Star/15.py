n=6
count=1
for i in range(n):
    for j in range(i):
        if count==0:
            print("0",end=" ")
            count=1
        else:
            print("1",end=" ")
            count=0
    print()

n=6
count=1
for i in range(n):
    for j in range(i):
        print(count,end=" ")
        count=1-count
    print()