#Take 5 numbers as input, skip any number that is 0 using continue, and calculate the sum of the remaining numbers.
'''
total=0
for i in range(5):
    take=int(input(f"Enter Number {i+1}: "))
    if take==0:
        continue
    total=total+take
print(total)
'''
num=0
total=0
while num<5:
    take=int(input(f"Enter Number {num+1}: "))
    if take==0:
        num=num+1
        continue
    total=total+take
    num=num+1
print(total)
