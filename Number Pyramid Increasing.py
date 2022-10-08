n = input("Enter last number : ")

for i in range(1,n+1):
    string = ""
    string += " " * (n-i)
    for j in range(1,i+1):
        string += str(j)
    for j in range(i-1,0,-1):
        string += str(j)
    print string
    
for k in range(n-1,0,-1):
    string = ""
    string += " " * (n-k)
    for l in range(1,k+1):
        string += str(l)
    for l in range(k-1,0,-1
    ):
        string += str(l)
    print string