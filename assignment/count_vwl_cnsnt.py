def count(string):
    vowels = 'AEIOUaeiou'
    num_vwl = 0
    num_cnsnt = 0
    for ch in string:
        if ch.isalpha():  
            if ch in vowels:
                num_vwl += 1
            else:
                num_cnsnt += 1
    return num_vwl, num_cnsnt
string = input("Enter a string: ")
vowels, consonants = count(string)
print("Number of vowels:",vowels)
print("Number of consonants:",consonants)
