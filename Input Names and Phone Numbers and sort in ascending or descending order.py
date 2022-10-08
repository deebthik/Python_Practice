n = input("Enter no. of students : ")
l = [[None, None] for i in range(n)]
print l

for i in range(n):
    l[i][0] = raw_input("Enter name : ")
    l[i][1] = raw_input("Enter phone no. : ")
    
    
print l
    
for i in range(n):
    for j in range(i+1, n):
        if(l[i][0] > l[j][0]):
            l[j], l[i] = l[i], l[j]
            
op = raw_input("Enter option(asc or desc) : ")

if(op == "asc"):
    for i in range(n):
        print l[i][0], "\t", l[i][1]
elif(op == "desc"):
    l_rev = []
    for i in l:
        l_rev = [i] + l_rev
    for i in range(n):
        print l_rev[i][0], "\t", l[i][1]