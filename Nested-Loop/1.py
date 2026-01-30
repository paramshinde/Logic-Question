#Print the multiplication tables for all numbers from 1 to 10
for i in range(1,11):
    table=0
    for j in range(1,11):
        print(i,'*',j,'=',i*j)
    print()