def triangle4(n):
    for i in range(1,n+1):
        for j in range(1,i):
            print(" ",end=" ")
        for j in range(i,n+1):
            print(i,end=" ")
        print()

n=int(input("Enter number of rows: "))
triangle4(n)
