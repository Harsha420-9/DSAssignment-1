# Write a Python program to count the number of even and odd numbers from a series of numbers.

# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

# Expected Output :

# Number of even numbers : 4

# Number of odd numbers : 5
low_Ran = int(input("lower range :"))
hig_ran = int(input("upper range :"))
count1 = 0
count2 = 0
for i in range(low_Ran,hig_ran+1):
    if i %2 == 0:
         count1 += 1
print("Number of even numbers :" ,count1)
for j in range(low_Ran,hig_ran+1):
    if j %2 != 0:
         count2 += 1
print("Number of odd numbers :" ,count2)