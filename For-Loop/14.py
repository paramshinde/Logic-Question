#Find the HCF (Highest Common Factor) of the given numbers.
n1=12
n2=18
limit=min(n1,n2)
hcf=0
for i in range(limit,1,-1):
    if n1%i==0 and n2%i==0:
        print("HCF: ",i)
        break




