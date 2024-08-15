def num_diamond(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ", end="")
        for j in range(1, i+1):
            print(j, end=" ")
        print()
    for i in range(n-1, 0, -1):
        for j in range(n - i):
            print(" ", end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

n=int(input("Enter number of rows: "))
num_diamond(n)
