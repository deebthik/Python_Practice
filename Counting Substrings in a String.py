n = str(raw_input("Enter string : "))
sub = str(raw_input("Enter substring : "))
l = 0

for i in n:
    if (i == sub):
        l += 1
        
print "The substring", sub, "occurs", l, "times in the word", "\'" + n + "\'