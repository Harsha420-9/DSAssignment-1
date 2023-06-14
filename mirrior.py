# Write a Python program that accepts a word from the user and reverse it.

# Sample Test Case

# Input : Edyoda

# output: adoydE

word = input('provide an Input :')
if len(word)>0:
    input = word[::-1]
    print('Reversed Input is :',input)
else:
    ('please provide some characters to mirror :')