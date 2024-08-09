def separate(lst):
    even=[]
    odd=[]
    for i in lst:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd
l=[int(x) for x in input("Enter a list of integers: ").split()]
even, odd = separate(l)
print("List of even numbers:", even)
print("List of odd numbers:", odd)



