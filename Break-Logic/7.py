#Continuously add numbers in a loop and stop the loop when the sum becomes greater than 100
n=0
total=0
while True:
    total=total+n
    if total>100:
        break
    print(total)
    n=n+1
