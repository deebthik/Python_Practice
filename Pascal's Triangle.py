import math

length = 0

def Combination(n, r):
    numerator = math.factorial(n)
    denominator =  math.factorial(r) * math.factorial(n - r)
    return int(numerator/denominator)
    
def Length(n):
    length = 0
    for i in str(n):
        length += 1
    return length

n = input("Enter the no. of rows : ")

for i in str(Combination(n, n/2)):
    length += 1

spaces = (n * length) - 2

for i in range(0, n):
    string = ""
    string += " " * spaces

    for j in range(0, i+1):
        string += str(Combination(i, j)) + " " * (length * 2 - Length(Combination(i, j)))
        
    print string
    spaces -= length