def sum_of_digits(n):
    s=0
    for digit in str(n):
        s+=int(digit)
    print("Sum of digits is: ",s)
n=int(input("Enter any number: "))  
sum_of_digits(n)
