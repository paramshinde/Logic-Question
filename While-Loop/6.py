#Calculate and print the sum of the first n natural numbers.
n=int(input("Enter the Natural NO:"))
i=1
dup=0
while i<=n: 
    dup=i+dup
    i=i+1
print(dup)