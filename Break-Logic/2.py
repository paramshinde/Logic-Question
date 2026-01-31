#Print numbers from 1 to 100, but skip all numbers that are divisible by 5 and continue printing the rest
n=1
while n<=100:
    if n%5==0:
        n=n+1
        continue
    print(n)
    n=n+1

for i in range(1,101):
    if i%5==0:
        continue
    print(i)
    