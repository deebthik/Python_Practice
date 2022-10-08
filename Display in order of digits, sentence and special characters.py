string = raw_input("Enter string : ")
digits = ""
sentence = ""
special = ""

for s in string:
    if((s == " ") or (ord(s) in range(65,91)) or (ord(s) in range(97,123))):
        sentence += s
    elif(ord(s) in range(48,58)):
        digits += s
    else:
        special += s

final_word = digits + sentence + special
print final_word