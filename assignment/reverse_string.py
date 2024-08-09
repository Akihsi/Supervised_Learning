def reverse(string):
    new=""
    for i in string:
        new=i+new
    print("Reversed string: ",new)
string=str(input("Enter a string: "))
reverse(string)




