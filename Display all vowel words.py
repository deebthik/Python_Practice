string = raw_input("Enter string : ")
string += " "
vowels = "aeiouAEIOU"
i1 = -1
i2 = 0
final_word = ""

for s in string:
    i1 += 1
    if(s == " "):
        if(string[i2] in vowels):
            final_word += string[i2:i1] + " "
        i2 = i1+1

print final_word
