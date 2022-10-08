power = input("Enter the power: ")
n = input("Enter the number: ")
s = 0
i = 1.0

while i <= power:
    s += (n**i)/i
    i += 1
    
print s
    