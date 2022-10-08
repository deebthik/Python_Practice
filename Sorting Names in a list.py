def sorting(l, op="asc"):
    if(op == "asc"):
        x = "<minimum"
    else:
        x = ">minimum"
    n_l = []
    while l:
        minimum = l[0]
        for i in l:
            if(eval("i"+x)):
                minimum = i
        n_l += [minimum]
        l = [m for m in l if m not in n_l]
    return n_l
    
n = input("Enter no. of students : ")
l = []
for i in range(n):
    l += [raw_input("Enter name : ")]
op = raw_input("Enter option (asc or desc): ")

print sorting(l, op)