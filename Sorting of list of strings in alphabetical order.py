string = raw_input("Enter string : ").lower()
string += " "
final_word = ""
i1 = -1
i2 = 0

for n in range(97,123):
    i1 = -1
    i2 = 0
    for s in string:
        i1 += 1
        if(s == " "):
            if(ord(string[i2]) == n):
                final_word += string[i2:i1] + " "
            i2 = i1 + 1

print "Ascending Order:", final_word

final_word = ""
        
for n in range(123,96,-1):
    i1 = -1
    i2 = 0
    for s in string:
        i1 += 1
        if(s == " "):
            if(ord(string[i2]) == n):
                final_word += string[i2:i1] + " "
            i2 = i1 + 1
            
print "Descending Order:", final_word
        


    
    
        

