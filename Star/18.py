res=65
n=5
for i in range(1,n+1):
    res=65
    for j in range(i):
        dup=chr(res)
        print(dup,end=" ")
        res=res+1
        
    print()