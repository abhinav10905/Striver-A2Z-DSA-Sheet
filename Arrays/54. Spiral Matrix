**QUESTION**
54. Spiral Matrix
Given an m x n matrix, return all elements of the matrix in spiral order.

**CONSTRAINTS
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

**CODE**
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        top=0
        bottom=len(matrix)-1
        left=0
        right=len(matrix[0])-1
        spiral=[]
        while top<=bottom and left<=right:
            for i in range (left,right+1):
                spiral.append(matrix[top][i])
            top+=1
            for j in range (top,bottom+1):
                spiral.append(matrix[j][right])
            right-=1
            if top<=bottom:
                for k in range (right,left-1,-1):
                    spiral.append(matrix[bottom][k])
                bottom-=1
            if left<=right:
                for l in range (bottom,top-1,-1):
                    spiral.append(matrix[l][left])
                left+=1
        return spiral

**ABOUT MY CODE**
Time:- O(m*n)
Space:- O(1)
Approach:- Matrix
