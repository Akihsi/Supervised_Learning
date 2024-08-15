def rhombus2(n):
    for i in range(1,n+1):
        for j in range(1,i):
            print(" ",end=" ")
        print("* "*n)

n=int(input("Enter number of rows: "))
rhombus2(n)
