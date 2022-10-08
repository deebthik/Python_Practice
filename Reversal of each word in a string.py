string = raw_input("Enter string : ")
string += " "
i1 = -1
i2 = 0
final_word = ""

for s in string:
    i1 += 1
    if(s == " "):
        if(i2 == 0):
            final_word += string[i1::-1]
            i2 = i1+1
        else:
            final_word += string[i1:i2-1:-1]
            i2 = i1+1
    
print "The original string:", string
print "The final string:", final_word