rows = input("Enter the maximum number of stars: ")
j = rows
k = rows
p = 1
for i in range(rows+1):
    print " " * k," *" *  i
    k-=1
while j > 1:
    j -= 1
    print " " * p," *" * j
    p +=1
