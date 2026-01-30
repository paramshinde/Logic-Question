n=5
res=65
for i in range(n):
    for j in range(n-i-1):
       print(" ",end=" ")
    for k in range(i*2+1):
        dup=chr(res)
        print(dup,end=" ")
        res=res+1
    print() 