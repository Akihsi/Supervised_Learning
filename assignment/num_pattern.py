def num_pattern(n):
    for i in range(1,n+1):
        print(str(i)*i,end = " ")
        print ()
n = int(input('Enter the number of rows: '))
num_pattern(n)
