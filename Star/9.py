#Print a Centered Pyramid of Stars

n=6
for i in range(0,n):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()