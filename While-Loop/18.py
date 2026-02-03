#Check whether the given number is a prime number.
given_num=3
num=1
count=0
while num<=given_num:
    if given_num%num==0:
        count=count+1
    num=num+1
if count==2:
    print(given_num,"Prime")
else:
     print("not")