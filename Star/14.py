n=8
count=0
for i in range(n):
    for j in range(i):
        count=count+1
        if count>9:
            count=0
        print(count,end=" ")
    print()
