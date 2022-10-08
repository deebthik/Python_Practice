n = input("Enter last number : ")

for i in range(n,0,-1):
    string = ""
    string += " " * (i-1)
    for j in range(n,i-1,-1):
        string += str(j)
    for j in range(i+1,n+1):
        string += str(j)
    print string
    
for k in range(2,n+1):
    string = ""
    string += " " * (k-1)
    for l in range(n,k-1,-1):
        string += str(l)
    for l in range(k+1,n+1):
        string += str(l)
    print string