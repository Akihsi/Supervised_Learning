def rhombus(n):
    for i in range(1,n+1):
        for j in range(1,n-i+1):
            print(" ",end=" ")
        print("* "*n)

n=int(input("Enter number of rows: "))
rhombus(n)


