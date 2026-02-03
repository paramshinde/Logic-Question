#Find and print the sum of the Fibonacci series up to n terms.
num=3
a=0
b=1
n=0
sum=0
while n<num:
    #print(a)
    c=a+b
    a=b
    b=c
    n=n+1
print(sum)