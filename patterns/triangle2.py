def triangle2(n):
    for i in range(1,n+1):
        for j in range(1,n-i+2):
            print(n-i+1,end=" ")
        print()
n=int(input("Enter number of rows: "))
triangle2(n)
