string = raw_input("Enter string : ")
lower = 0
upper = 0
alphabets = 0
digits = 0
vowels = 0
consonants = 0
special = 0
v = "aeiouAEIOU"

for s in string:
    if(ord(s) in range(48, 58)):
        digits += 1
    else:
        if(ord(s) in range(65, 91)):
            alphabets += 1
            upper += 1
            if(s not in v):
                consonants += 1
            else:
                vowels += 1
                
        elif(ord(s) in range(97, 123)):
            alphabets += 1
            lower += 1
            if(s in v):
                vowels += 1
            else:
                consonants += 1
        
        else:
            special += 1
            
print "Lowercase alphabets :",lower
print "Uppercase alphabets :",upper
print "Digits :",digits
print "Alphabets :",alphabets
print "Vowels :",vowels
print "Consonants :",consonants
print "Special characters :",special