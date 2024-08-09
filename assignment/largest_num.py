def largest_num(lst):
   lrgst=lst[0]  
   for i in lst:
        if i>lrgst:
            lrgst=i
   return lrgst
l=[int(x) for x in input("Enter a list of integers: ").split()]
print("Largest number in the list:",largest_num(l))

