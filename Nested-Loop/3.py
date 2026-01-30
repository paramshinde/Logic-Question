#For every number from 1 to n, count and print the total number of its factors.
num=5
for i in range(1,num+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count=count+1
    print(i,count)