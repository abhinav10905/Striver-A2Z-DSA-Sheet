**QUESTION**
707. Find row with maximum 1's
Given a non-empty grid mat consisting of only 0s and 1s, where all the rows are sorted in ascending order, find the index of the row with the maximum number of ones.
If two rows have the same number of ones, consider the one with a smaller index. If no 1 exists in the matrix, return -1.

**CONSTRAINTS**
n == mat.length 
m == mat[i].length 
1 <= n, m <= 100 
mat[i][j] is either 0 or 1.

**CODE**
class Solution:
    def rowWithMax1s(self, mat):
        c=-1
        d=0
        for i in mat:
            low=0
            high=len(i)
            while low<high:
                mid=(low+high)//2
                if i[mid]==0:
                    low=mid+1
                else:
                    high=mid
            if len(i)-low>d:
                d=len(i)-low
                c=mat.index(i)
        return c

**ABOUT MY CODE**
Time:- O(n*logm)
Space:- O(1)
Approach:- Binary Search
