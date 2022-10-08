rows = input("Enter the maximum number of stars: ")

for r in range(rows+1):
    for i in range(r):
        print "*",
    print
    

    
for r in range((rows-1), 0, -1):
    for i in range(r):
        print "*",
    print