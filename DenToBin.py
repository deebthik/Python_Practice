def DenToBin(n):
    r = ""
    while(n!=1):
        r = str(n%2) + r
        n /= 2
    r = "1" + r
    return r
    
n = input("Enter the denary number : ")
print "The binary of", n, "is", DenToBin(n)