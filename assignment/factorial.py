def factorial(n):
    fact=1
    if n<0:
        print("Factorial of negative number is not defined.")
    else:
        for i in range(1,n+1):
            fact*=i
        print("Factorial of ",n,":",fact)
n=int(input("Enter any number: "))
factorial(n)
