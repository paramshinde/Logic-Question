#Print Stars in Odd Numbers (1, 3, 5, 7, 9)
n=6
for i in range(n):
    for j in range(2*i+1):
        print("*",end=" ")
    print() 