i = 1
s = 0

while(i<=1000):
    s = 0
    char = str(i)
    for r in char:
        s += pow((int(r)), 3)
    if s== int(i):
        print i
    i+= 1