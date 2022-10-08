l = input("Length : ")
b = input("Breadth : ")

print "*" * l
print

for i in range(1,(b/2)+1):
    print "*" + " " * (l-2) + "*"
    print 
    
print "*" * l