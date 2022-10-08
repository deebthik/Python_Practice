string = raw_input("Enter string : ")

print "The reverse is", string[-1::-1]

if(string[-1::-1] == string):
    print "It is a palindrome"
else:
     print "It is not a palindrome"   