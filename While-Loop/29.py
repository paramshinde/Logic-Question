#Find the largest digit in the given number.
num=834
large=0
while num>0:
    digit=num%10
    if digit>large:
        large=digit
    num=num//10
print(large)
