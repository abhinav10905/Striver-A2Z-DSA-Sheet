**QUESTION**
118. Pascal's Triangle
Given an integer numRows, return the first numRows of Pascal's triangle.

**CONSTRAINTS**
1 <= numRows <= 30

**CODE**
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        else:
            a=[[1],[1,1]]
            j=2
            while j<numRows:
                b=[1]
                for i in range (0,len(a[-1])-1):
                    c=a[-1][i]+a[-1][i+1]
                    b.append(c)
                b.append(1)
                a.append(b)
                j+=1
            return a
        
**ABOUT MY CODE**
Time:- O(n**2)
Space:- O(n**2)
Approach:- DP, Array
