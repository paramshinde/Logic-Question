#Print Repeated Numbers per Row (Same Number Repeated)

n=6
for i in range(1,n):
    for j in range(i):
        print(i,end="")
    print()