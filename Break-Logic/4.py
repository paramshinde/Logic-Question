#Search for a specific number in a list of inputs, and terminate the loop immediately when the number is found.
'''
spec=4
for i in range(6):
    num=int(input(f"Enter Number {i}: "))
    if num==spec:
        break
    print(num)
'''
num=0
spec=3
while num<6:
    take=int(input(f"Enter Number {num+1} :"))
    if take==spec:
        break
    print(take)
    num=num+1