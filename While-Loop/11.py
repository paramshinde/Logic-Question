#Count and print the total number of digits in a given number.
num=123412
count=0
while num>0:    
    count=count+1
    num=num//10
print(count)