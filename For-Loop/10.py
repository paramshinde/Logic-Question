#Print the Fibonacci series up to the required number of terms.
num=10
a=0
b=1

for i in range(num):
    print(a ,end=" ")
    c=a+b
    a=b
    b=c

