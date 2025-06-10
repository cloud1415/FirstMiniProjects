n = int(input("Enter number of rows : "))

if n%2 == 0 :
    print("Choose odd number")
    exit()

blankSpace = int((n-1)/2)

# I method

for i in range(n):
    print(" " * abs(blankSpace-i), end = "")
    
    if i <= blankSpace: print("* " * (i+1))
    else: print("* " * (n-i))

# II method
for i in range(n):
    print(" " * abs(blankSpace-i), end = "")
    print("* " * (min(i+1, n-i)))
    
