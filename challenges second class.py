# K
bows = int(input("Enter number of rows: "))

for i in range(bows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")

n = int(4)

for i in range(1,2*n):
    for j in range(1,2*n):
        if i==j or i+j==2*n:
            print('*', end='')
        else:
            print(' ', end='')
    print()