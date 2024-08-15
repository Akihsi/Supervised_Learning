def triangle3(n):
    for i in range(1,n+1):
        for j in range(i,n):
            print(" ",end=" ")
        for i in range(1,i+1):
            print(i,end=" ")
        print()
        
n=int(input("Enter number of rows: "))
triangle3(n)
