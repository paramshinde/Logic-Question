#Print Stars in Even Numbers (2, 4, 6, 8, 10 )
n=6
for i in range(1,n):
    for j in range(2*i):
        print("*",end="")
    print()