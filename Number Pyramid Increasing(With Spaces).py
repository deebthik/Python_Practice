n = input("Enter last number : ")

spaces = n+(n-2)

for i in range(1,n+1):
    string = ""
    string += " " * spaces
    for j in range(1,i+1):
        string += str(j) + " "
    for j in range(i-1,0,-1):
        string += str(j) + " "
    print string
    print
    spaces -= 2
    
spaces = 2

for k in range(n-1,0,-1):
    string = ""
    string += " " * spaces
    for l in range(1,k+1):
        string += str(l) + " "
    for l in range(k-1,0,-1):
        string += str(l) + " "
    print string
    print
    spaces += 2