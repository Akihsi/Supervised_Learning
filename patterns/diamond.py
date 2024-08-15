def diamond(n):
    n=n//2+1
    for i in range(1,n+1):
        for j in range(i,n):
            print(" ",end="")
        for k in range(1,i+1):
            print("*",end=" ")
        print()
    for i in range(1,n):
        for j in range(1,i+1):
            print(" ",end="")
        for k in range(i,n):
            print("*",end=" ")
        print()        
 
n=int(input("Enter number of rows: "))
diamond(n)
