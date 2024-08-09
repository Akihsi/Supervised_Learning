def fibonacci(n):
    n1,n2=0,1
    count=0
    if n<=0:
        print("Enter a postive interger, given input is not valid.")
    else:
        print ("The Fibonacci sequence upto",n,"terms: ")  
        for i in range(0,n):
            print(n1,end=", ")
            n3=n1+n2
            n1,n2=n2,n3
n=int(input("Enter any number: "))
fibonacci(n)
