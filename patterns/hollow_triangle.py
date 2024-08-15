def hollow_tri(n):
    for i in range(1,n+1):
        for j in range(i,n+1):
            if i==1 or j==n or j==i:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
n=int(input("Enter number of rows: "))
hollow_tri(n)
