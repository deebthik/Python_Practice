def anchor(matrix):
    d1 = []
    d2 = []
    for i in range(len(matrix)):
        d1 += [matrix[i][i]]
        d2 += [matrix[i][len(matrix)-i-1]]
    l = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            l += [matrix[i][j]]
        print l
        n_l = []
        while l:
            minimum = l[0]
            for k in l:
                if(k<minimum):
                    minimum = k
            n_l += [minimum]
            l = [m for m in l if m not in n_l]
        print n_l
        print i+1, "min.", n_l[0]
        print i+1, "max.", n_l[len(n_l)-1]
        if(n_l[0] in d1 or n_l[0] in d2):
            print "It is part of the diagonals"
        print
        print

n = input("Enter limit : ")        
matrix = [[None for i in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        matrix[i][j] = input("Enter value : ")

print matrix
print

anchor(matrix)