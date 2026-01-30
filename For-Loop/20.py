#Find and print the sum of all even numbers from 1 up to n
num=5
res=0
for i in range(1,num+1):
    if i%2==0:
        res=res+i
print(res)