n = input("Enter limit : ")
matrix = [[None for i in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        matrix[i][j] = input("Enter element : ")
        
print matrix

for k in range(n):
    for i in range(n):
        for j in range(i+1, n):
            if(matrix[k][i] > matrix[k][j]):
                matrix[k][i], matrix[k][j] = matrix[k][j], matrix[k][i]
            
for i in range(n):
    for j in range(n):
        print matrix[i][j],
    print