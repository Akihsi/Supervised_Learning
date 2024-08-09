def ispalindrome(string):
    for i in range(len(string)//2):
        if string[i]!=string[-1-i]:
            return False
    return True
string=str(input("Enter a string: "))
print("String is a palidrome:",ispalindrome(string))




