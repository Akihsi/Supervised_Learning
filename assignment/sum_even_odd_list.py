def sum_even_odd(lst):
    sum_even=sum(x for x in lst if x%2==0)
    sum_odd=sum(x for x in lst if x%2!=0)
    return (sum_even, sum_odd)
l=[int(x) for x in input("Enter list of numbers: ").split()]
print("Sum of even and odd numbers in the list: ",sum_even_odd(l))


