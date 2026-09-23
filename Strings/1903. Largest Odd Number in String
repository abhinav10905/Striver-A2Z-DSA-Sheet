**QUESTION**
1903. Largest Odd Number in String
You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.
A substring is a contiguous sequence of characters within a string.

**CONSTRAINTS**
1 <= num.length <= 105
num only consists of digits and does not contain any leading zeros.

**CODE**
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range (len(num)-1,-1,-1):
            if int(num[i])%2!=0:
                return num[:i+1]
        return ""
        
**ABOUT MY CODE**
Time:- O(n)
Space:- O(1)
Approach:- String
