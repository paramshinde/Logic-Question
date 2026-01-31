n=4
count=1
for i in range(n+1):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(i*2+1):
        print(count,end=" ")
        count=count+1
    print()
    count=1
    