word = raw_input("Enter String : ")
string = word
final_word = ""
i = -1

for s in string:
    i += 1
    if(i == 0):
        final_word += chr(ord(s) - 32)
    else:    
        if(string[i-1] == " "):
            final_word += chr(ord(s) - 32)
        else:
            final_word += s
            
print final_word