string = raw_input("Enter string : ")
final_word = ""
i = -1

for s in string:
    i += 1
    if(ord(s) in range(65,91) or ord(s) in range(97,123)):
        if(i%2!=0):
            final_word += chr(ord(string[i]) - 32)
        else:
            final_word += string[i]
    else:
        final_word += string[i]
        
print final_word
