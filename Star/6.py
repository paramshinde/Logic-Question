#Print a Right-Aligned Triangle of Stars
from time import sleep
n=6
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="",flush=True)
        sleep(0.3)
    for k in range(i):
        print("*",end="",flush=True)
        sleep(0.2)
    print()