def Encrypt_Decrypt(string, ak1, ak2):
    final_word = ""
    for s in string:
        if(s in alphabet):
            n = ak1.find(s)
            final_word += ak2[n]
        else:
            final_word += s
    return final_word

alphabet = "abcdefghijklmnopqrstuvwxyz"
key = "xznlwebgjhqdyvtkfuompciasr"

option = "Y"

while(option == "Y"):
    print "1. Encrypt"
    print "2. Decrypt"
    op = input("Enter the serial no. of the option : ")
    
    if(op == 1):
        string = raw_input("Enter decrypted/original string (lowercase) : ").lower()
        print "The encrypted string is", Encrypt_Decrypt(string, alphabet, key)
        
    if(op == 2):
        string = raw_input("Enter encrypted string (lowercase) : ").lower()
        print "The decrypted string is", Encrypt_Decrypt(string, key, alphabet)
        
    option = raw_input("Do you want to continue using the program (Y or N) : ")
    
else:
    print "Goodbye :)"