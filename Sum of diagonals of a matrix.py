n = input("Enter limit of matrix : ")
matrix = []

for i in range(n):
    l = list(input("Enter list : "))
    matrix += [l]

print matrix

ls = 0
rs = 0

k = 0
l = len(matrix)-1

for i in matrix:
    ls += matrix[k][k]
    rs += matrix[k][l]
    k += 1
    l -= 1
        
print ls, "is the sum of the left diagonal"
print rs, "is the sum of the right diagonal"