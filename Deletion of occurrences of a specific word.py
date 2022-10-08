string = raw_input("Enter string : ")
string_l = list(string)
sub = raw_input("Enter sub-string : ")
i = -1

for s in string_l:
    i += 1
    if(s == sub[0]):
        if(string[i:i+len(sub)] == sub):
            string_l[i:i+len(sub)] = ""
            
final_word = ""
i = -1

for s in string_l:
    final_word += s
    
print "The final word is", final_word