l = list(input("Enter list : "))
n_l = []

for i in l:
    if(i<0):
        n_l = [i] + n_l
    elif(i>=0):
        n_l += [i]
        
print n_l