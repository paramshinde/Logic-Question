#Find the HCF (Highest Common Factor) of two given numbers.
a=45
b=30
limit=max(a,b)
n=1
HCF=0
while n<=limit:
    if a%n==0 and b%n==0:
        HCF=n
        #break
    n=n+1
print(HCF)