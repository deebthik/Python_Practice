a=[]
n=input ("The limit of List:- ") 
print
for i in range(0,n):
    c=list(input("Enter Numbers in the List:- "))
    a += [c]
print a
for i in range(0,len(a)):
    for j in range(0,len(a[i])):
        print a[j][i], 
    print