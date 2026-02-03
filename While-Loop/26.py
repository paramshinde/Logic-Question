#Find the HCF (Highest Common Factor) of two given numbers.
a=45
b=30
limit=min(a,b)
HCF=0
while limit>0:
    if a%limit==0 and b%limit==0:
        print(limit)
        break
    limit=limit-1
