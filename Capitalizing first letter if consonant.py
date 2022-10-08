string = raw_input("Enter string : ")
final_word = ""
i = -1
vowels = "aeiouAEIOU"

for s in string:
    i += 1
    
    if(s not in vowels):
        if(i == 0):
            final_word += chr(ord(s) - 32)
        else:
            if(string[i-1] == " "):
                final_word += chr(ord(s) - 32)
            else:
                final_word += s
    else:
        final_word += s
                
print final_word