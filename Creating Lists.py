n = input("Enter limit : ")
matrix = []

for i in range(n):
    l = list(input("Enter list : "))
    matrix += [l]
    

    
for i in matrix:
    for j in i:
        print j,
    print