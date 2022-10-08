i = 1
n = input("Enter no. of rows : ")
while(i <= n):
    if(i%2 != 0):
        print "#" * i
    if(i%2 == 0):
        print "@" * i
    i += 1