#Calculate and print the factorial of every number from 1 to n
num=5
res=1
for i in range(1,num+1):
    res=res*i
    print(i,"! = ",res)
