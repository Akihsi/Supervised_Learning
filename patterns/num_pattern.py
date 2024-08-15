def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        for j in range(i*2,n*2):
            print(" ",end=" ")
        for j in range(i,0,-1):
            print(j,end=" ")
        print()
        
n=int(input("Enter number: "))
pattern(n)
