**QUESTION**
509. Fibonacci Number
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

**CONSTRAINTS**
0 <= n <= 30

**CODE**
class Solution:
    def fib(self, n: int) -> int:
        a=0
        b=1
        if n==0:
            return a
        elif n==1:
            return b
        else:
            i=1
            c=0
            while i<n:
                c=a+b
                a=b
                b=c
                i+=1
            return b
        
**ABOUT MY CODE**
Time:- O(n)
Space:- O(1)
Approach:- Math
