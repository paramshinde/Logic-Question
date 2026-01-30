#Find and print the sum of all factors of the given number
num=10
sum=0
for i in range(1,num+1):
    if num%i==0:
        sum=sum+i
print(sum)