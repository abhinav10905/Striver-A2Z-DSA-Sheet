**QUESTION**
921. Minimum Add to Make Parentheses Valid
A parentheses string is valid if and only if:
It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.
For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.

**CONSTRAINTS**
1 <= s.length <= 1000
s[i] is either '(' or ')'.

**CODE**
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        a=0
        c=0
        for i in s:
            if i=="(":
                a+=1
            else:
                a-=1
                if a<0:
                    c+=1
                    a+=1
        c+=a
        return c
        
**ABOUT MY CODE**
Time:- O(n)
Space:- O(1)
Approach:- String  
