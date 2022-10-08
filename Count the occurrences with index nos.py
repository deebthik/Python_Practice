string = raw_input("Enter string : ")
sub = raw_input("Enter sub-string : ")
string_l = list(string)
len_sub = len(sub)
n = 0
start = []
end = []
i = -1

for s in string_l:
    i += 1
    if(s == sub[0]):
        if(string[i:i+len_sub] == sub):
            n += 1
            start +=  [i]
            end += [i + len_sub - 1]
            
print "The no. of occurrences :", n
print "The starting index nos.:", start
print "The ending index nos.:", end