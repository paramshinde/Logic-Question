#Find and print the sum of the Fibonacci series.
num=5
a=0
b=1
res=0
for i in range(num):
    res=res+a
    print(a)
    c=a+b
    a=b
    b=c

print("The Sum is: ",res)