**QUESTION**
1901. Find a Peak Element II
A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.
Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].
You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.
You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

**CONSTRAINTS**
m == mat.length
n == mat[i].length
1 <= m, n <= 500
1 <= mat[i][j] <= 105
No two adjacent cells are equal.

**CODE**
class Solution:
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        m=len(mat)
        n=len(mat[0])
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            r=0
            for i in range (1,m):
                if mat[i][mid]>mat[r][mid]:
                    r=i
            if mid!=0:
                left=mat[r][mid-1]
            else:
                left=-1
            cur=mat[r][mid]
            if mid!=n-1:
                right=mat[r][mid+1]
            else:
                right=-1
            if left<cur and right<cur:
                return [r,mid]
            elif left>cur:
                high=mid-1
            else:
                low=mid+1
        return [-1,-1]

**ABOUT MY CODE**
Time:- O(mlogn)
Space:- O(1)
Approach:- Binary Search
