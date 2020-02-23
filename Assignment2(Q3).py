'''
Given an integer n, return the length of the longest 
consecutive run of 1s in its binary representation.
For example, given 156, you should return 3

explanation 
binary of 156 (bin(156)) is '0b10011100'
there are max consecutive 1s is 3 

sample input
12
sample output
2
'''

def maxOnesConsec(n):
    c = 0
    while (n!=0):
        n = (n & ( n << 1))

        c = c + 1

    return c
print(maxOnesConsec(int(input()))
