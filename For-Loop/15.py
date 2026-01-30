#Find the LCM (Least Common Multiple) of the given numbers
n1=21
n2=18
lcm=0

start=max(n1,n2)
end=n1*n2
for i in range(start,end+1,start):
    if i%n1==0 and i%n2==0:
        print("LCF",i)
        break
    