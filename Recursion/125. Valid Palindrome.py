**QUESTION**
125. Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

**CONSTRAINTS**
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

**CODE**
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        m="true"
        for i in s:
            if ord(i)>=97 and ord(i)<=122:
                a=a+i
            elif ord(i)>=48 and ord(i)<58:
                a=a+i
            elif ord(i)>=65 and ord(i)<91:
                c=i.lower()
                a=a+c
            else:
                pass
        i=0
        j=len(a)-1
        while i<=j:
            if a[i]!=a[j]:
                m="false"
                break
            i+=1
            j-=1
        if m=="true":
            return True
        else:
            return False

**ABOUT MY CODE**
Time:- O(n)
Space:- O(n)
Approach:- String, ASCII
        
