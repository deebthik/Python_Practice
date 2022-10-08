def DenToOctal(n):
    r = ""
    run = True
    while(run):
        r = str(n%8) + r
        n /= 8
        if(n <= 7):
            break
    r = str(n) + r
    return r
    
n = input("Enter the denary number : ")
print "The octal of", n, "is", DenToOctal(n)