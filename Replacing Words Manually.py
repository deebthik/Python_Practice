word = raw_input("Enter string : ")
string = word
s1 = raw_input("Enter the sub-string which is to be replaced : ")
s2 = raw_input("Enter the sub-string with the first sub-string is to replaced : ")

string_l = list(string)

while (string.find(s1) != -1):
    n = string.find(s1)
    string_l[n:n+len(s1)] = list(s2)
    string = "".join(string_l)
    
print "".join(string)



    