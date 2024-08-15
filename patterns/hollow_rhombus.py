def hol_rh(n):
    for i in range(1,n+1):
        for j in range(1,n-i+1):
            print(" ",end=" ")
        for k in range(1,n+1):
            if i==1 or i==n or k==1 or k==n:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        
def hol_rh2(n):
    for i in range(1,n+1):
        for j in range(1,i):
            print(" ",end=" ")
        for k in range(1,n+1):
            if i==1 or i==n or k==1 or k==n:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
n=int(input("Enter number of rows: "))
hol_rh(n)
print()
hol_rh2(n)
