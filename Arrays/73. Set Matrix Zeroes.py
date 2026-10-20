**QUESTION**
73. Set Matrix Zeroes
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

**CONSTRAINTS**
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1

**FOLLOW UP**
A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

**CODE**
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=len(matrix[0])
        row=[0]*n
        column=[0]*m
        for i in range (0,n):
            for j in range (0,m):
                if matrix[i][j]==0:
                    row[i]=1
                    column[j]=1
        for i in range (0,n):
            for j in range (0,m):
                if row[i]==1 or column[j]==1:
                    matrix[i][j]=0
        

**ABOUT MY CODE**
Time:- O(n*m)
Space:- O(n+m)
Approach:- Array, Matrix
