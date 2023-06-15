# The Fibonacci Sequence is the series of numbers :

# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....

# Every next number is found by adding up the two numbers before it.

# Expected Output : 1 1 2 3 5 8 13 21 34

sum = 0
n1,n2 = 0,1
num = 50
for i in range(0,num):
    n1=n2
    n2=sum
    sum=n1+n2
    print(sum)
if num<=0:
    print('enter number greater than zero ')
