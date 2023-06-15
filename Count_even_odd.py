# Write a Python program to count the number of even and odd numbers from a series of numbers.

# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

# Expected Output :

# Number of even numbers : 4

# Number of odd numbers : 5
numbers_list = [int(num) for num in input("Enter a series of numbers : ").split()]
even_count = 0
odd_count = 0

for num in numbers_list:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
