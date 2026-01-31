#Keep taking numbers from the user and print them until a negative number appears, then stop the loop.
'''
n=10
for i in range(n):
    num=int(input(f"Enter Number {i+1}: "))
    if num<0:
        break
    print(num)
'''
i=0
while True:
    num=int(input(f"Enter Num{i+1} :"))
    if num<0:
        break
    print(num)
    i=i+1