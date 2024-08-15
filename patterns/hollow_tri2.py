def hollow_tri2(n):
    for i in range(1,n+1):
        for j in range(i,n):
            print(" ",end=" ")
        for k in range(1,2*i):
            if i==n or k==1 or k==2*i-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
n=int(input("Enter number of rows: "))
hollow_tri2(n)
