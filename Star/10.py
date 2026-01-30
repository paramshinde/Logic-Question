#Print Stars and Spaces Alternating (Stars and Blank Spaces) (b = blank space here)
n=6
for i in range(0,n):
    for j in range(n-i):
        print("b",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()