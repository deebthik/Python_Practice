i = 1
n = input("Enter max. number : ")
j = 1
s = 0
k = n-1
l = 1

while(i<=n):
    print " " * (n-i),
    for j in range(1, i+1):
        print "\b"+str(j),
    for j in range(i-1, 0, -1):
        print "\b"+str(j),
    print
    i += 1
    
while(k>=1):
    print " " * (n-k),
    for l in range(1, k+1):
        print "\b"+str(l),
    for l in range(k-1, 0, -1):
        print "\b"+str(l),
    print
    k -= 1
    