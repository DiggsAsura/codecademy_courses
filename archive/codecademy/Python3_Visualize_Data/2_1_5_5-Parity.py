# 2. Python for Data Analysis
# 1. Python Lists
# 5. List Comprehension - Code Challenge
# 5. Parity

''' 
In Python, %, or the modulo function, returns a remainder after a division.

4%2
0

7%3
1

27%10
7

30%10
0

You can use %2 to determine if a number is even or odd. If it is even, there 
should be no remainder (an outputof 0). If it is odd, there should be a remainder
of 1:

4%2
0

7%2
1

9%2
2

0%2
0

'''

nums = [4, 8, 15, 16, 23, 42]
parity = [num%2 for num in nums]
print(parity)