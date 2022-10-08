string = raw_input("Enter string : ")
string += " "
l = []
i1 = -1
i2 = 0

for s in (string):
    word = ""
    i1 += 1
    if (s == " "):
        for n in range(i2, i1):
            word += string[n]
        l += [word]
        i2 = i1+1
        
print l