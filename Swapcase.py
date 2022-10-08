string = raw_input("Enter string : ")
final_word = ""
i = -1

for s in string:
    i += 1
    if(ord(string[i]) in range(65,91)):
        final_word += chr(ord(string[i]) + 32)
    elif(ord(string[i]) in range (97,123)):
        final_word += chr(ord(string[i]) - 32)
    else:
        final_word += string[i]
        
print final_word