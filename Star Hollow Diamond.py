width = input("Enter max width : ")
n = width/2
spaces = 1

for i in range(1,n+1):
    if(i == 1):
        print " " * (n-i) + "*"
        continue
    print " " * (n-i) + "*" + " " * spaces + "*"
    spaces += 2
    
spaces -= 4

for j in range(n-1,0,-1):
    if(j == 1):
        print " " * (n-j) + "*"
        continue
    print " " * (n-j) + "*" + " " * spaces + "*"
    spaces -= 2
    