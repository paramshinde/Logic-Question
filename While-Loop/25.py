#Find and print the sum of all factors of the given number.
num=8
n=1
total=0
while n<=num:
    if num%n==0:
        total=total+n
    n=n+1
print(total)