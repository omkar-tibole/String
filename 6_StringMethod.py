a=" hello !"



# # String Methods in Python

# convert string to upper case
print(a.upper())


# convert string to lower case
print(a.lower())


# find the index of a character
print(a.find("h"))


# isalnum() checks if all characters are alphanumeric
b="hello123"
print(b.isalnum())


# split() splits the string into a list of words
print(a.split(" "))


# index() returns the index of the first occurrence of a character
print(a.index("o"))


# isupper() checks if all characters are uppercase
print(a.isupper())


# islower() checks if all characters are lowercase
print(a.islower())


# center() centers the string within a specified width
print(a.center(50))


# isspace() checks if the string contains only whitespace characters
print(a.isspace())


# capitalize() capitalizes the first character of the string
print(a.capitalize())


# istitle() checks if the string is in title case
print(a.istitle())


# isprintable() checks if all characters in the string are printable
print(a.isprintable())


# replace() replaces is used to replace a substring with another substring
print(a.replace("h", "omkar "))


# strip() removes leading and trailing whitespace characters
print(a.strip(" "))


# rstrip() removes trailing whitespace characters
print(a.rstrip("!"))


# isalpha() checks if all characters in the string are alphabetic
print(a.isalpha())


# count() counts the value of a specific character in the string
print(a.count("l"))


# swapcase() swaps is used to swap the case of all characters in the string
print(a.swapcase())


# title() converts the first character of each word to uppercase
print(a.title())


# endswith() checks if the string ends with a specified substring
print(a.endswith("!"))


# startswith() checks if the string starts with a specified substring
print(a.startswith(" "))




# Write a program that takes a string from the user and prints it in uppercase.


a=str(input("Enter a string: ").upper())
print(a)

a=str(input("Enter a string: "))
print(a.upper())





# Write a program that takes a string from the user and counts the number of consonant in it.
# a=str(input("Enter a string: "))

# a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a="abcdefghijklmnopqrstuvwxyz"
b=input("Enter a String: ")

count=0

for j in a:
    if j in b:
        count+=1
print("This string has", count, "consonants.")
            



# Write a program that takes a string from the user and counts the number of vowels in it.

a="aeiouAEIOU"
b=input("Enter a String: ")

count=0

for j in a:
    if j in b:
        count+=1
print("This string has", count, "vowels.")


# Write a program that takes a string from the user and prints it in reverse.
a=input("Enter a String : ")
print(a[::-1])


# Write a program that takes a string from the user and checks if it is a palindrome.
a=input("Enter a string : ")
c=a[::-1]

if a==c:
    print("This is a polindrome")
else:
    print("This is not a polindrome")
# Write a program that takes a string from the user and counts the number of spaces in it.

a=input("Enter a string : ").count(" ")
print(a)

 
        

# Write a program that takes a string from the user and capitalizes the first letter of every word.
a=input("Enter a string : ").capitalize()
print(a)


# Write a program that takes a string from the user and counts how many times the letter 'a' appears.

a=input("Enter a string : ").count("a")
print(a)


# Write a program that takes two strings from the user and checks if they are equal.

a=input("Enter first string : ")
b=input("Enter second string : ")

if a==b:
    print("are equal")
else:
    print("are not equal")

# Write a program that takes a string from the user and removes all digits from it.
a=input("Enter a string")#.rstrip("0123456789")
# print(a)
s="".join([char for char in a if char not in "0123456789"])
print(s)

