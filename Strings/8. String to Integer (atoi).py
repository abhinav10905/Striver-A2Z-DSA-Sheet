**QUESTION**
8. String to Integer (atoi)
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
The algorithm for myAtoi(string s) is as follows:
Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.

 **CONSTRAINTS**
0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

**CODE**
class Solution:
    def myAtoi(self, s: str) -> int:
        a=""
        j=0
        while j<len(s):
            if s[j]==" ":
                j+=1
            else:
                break
        for i in range (j,len(s)):
            z=len(a)
            if i==j and (s[i]=="-" or s[i]=="+"):
                pass
            elif z==0 and s[i]=="0":
                pass
            elif ord(s[i])<48 or ord(s[i])>57:
                break
            else:
                a=a+s[i]
        if len(a)==0:
            a="0"
        d=0
        i=0
        while i<len(a)-1:
            d+=int(a[i])
            d*=10
            i+=1
        d+=int(a[-1])
        if j!=len(s) and s[j]=="-":
            return max(-2**31,min(2**31-1,-d))
        else:
            return max(-2**31,min(2**31-1,d))

**ABOUT MY CODE**
Time:- O(n)
Space:- O(n)
Approach:- String  
