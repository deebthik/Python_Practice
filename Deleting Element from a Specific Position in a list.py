l = list(input("Enter list : "))
p = input("Enter position : ")-1
new_list = []

for i in range(len(l)):
    if(i != p):
        new_list += [l[i]]
        
print new_list
