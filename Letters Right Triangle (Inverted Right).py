rows = input("Enter the maximum number of letters: ")

for r in range(rows+1):
    char = "A"
    for i in range(r):
        print char,
        char = chr(ord(char) + 1)
    print
    