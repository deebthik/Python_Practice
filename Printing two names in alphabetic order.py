'''def Comparison(len_name, name1, name2):
    final_string = ""
    for i in range(len_name):
        if(name1[i] > name2[i]):
            final_string += name2 + ", " + name1
            break
        if(name1[i] < name2[i]):
            final_string += name1 + ", " + name2
            break
    return final_string

name1 = raw_input("Enter first name : ")
name2 = raw_input("Enter second name : ")
final_string = ""

if(name1 != name2):
    if(len(name1) == len(name2)):
        print Comparison(len(name1), name1, name2)
    if(len(name1) > len(name2)):
        print Comparison(len(name2), name1, name2)
    if(len(name1) < len(name2)):
        print Comparison(len(name1), name1, name2)
else:
    print name1 + ", " + name2'''
    
name1 = raw_input("Enter first name : ")
name2 = raw_input("Enter second name : ")

if(name1 < name2):
    print name1 + ", " + name2
elif(name1 > name2):
    print name2 + ", " + name1
else:
    print name1 + ", " + name2