#Generate and print a number triangle pattern using nested loops.
num=10
for i in range(0,num+1):
    for j in range(0,i+1):
        print(j,end=" ")
    print()