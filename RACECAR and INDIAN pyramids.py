string = raw_input("Enter string : ")
l = len(string)
p = l/2

if(l%2==0):
    for i in range(1, p+1):
        s = " " * (p-i)
        for j in range(i, 1, -1):
            s += string[p-j]
        s += string[p-1] + string[p]
        for j in range(1, i):
            s += string[p+j]
        print s

elif(l%2!=0):
    for i in range(p+1):
        s = " " * (p-i)
        for j in range(i, 0, -1):
            s += string[p-j]
        s += string[p]
        for j in range(1, i+1):
            s += string[p+j]
        print s
    