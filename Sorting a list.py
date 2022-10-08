l = list(input("Enter list : "))
new_list = []

while l:
    minimum = l[0]  # arbitrary number in list 
    for i in l: 
        if i < minimum:
            minimum = i
    new_list += [minimum]
    l = [i for i in l if i not in new_list]  

print new_list