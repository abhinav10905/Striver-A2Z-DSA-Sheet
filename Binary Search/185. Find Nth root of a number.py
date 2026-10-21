**QUESTION**
185. Find Nth root of a number
Given two numbers N and M, find the Nth root of M. The Nth root of a number M is defined as a number X such that when X is raised to the power of N, it equals M. If the Nth root is not an integer, return -1.

**CONSTRAINTS**
1 <= N <= 30
1 <= M <= 109

**CODE**
class Solution:
    def ans(self,a,n):
        return a**n
    def NthRoot(self, n, m):
        low=0
        high=m
        z=-1
        while low<=high:
            mid=(low+high)//2
            k=self.ans(mid,n)
            if k<m:
                low=mid+1
            elif k==m:
                return mid
            else:
                high=mid-1
        return z

**ABOUT MY CODE**
Time:- O(log(m))
Space:- O(1)
Approach:- Binary Search, Recursion
