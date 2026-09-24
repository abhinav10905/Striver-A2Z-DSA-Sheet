**QUESTION**
13. Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

**CONSTRAINTS**
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].

**CODE**
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        sum=0
        while i<len(s):
            if s[i]=="I":
                if i<len(s)-1:
                    if s[i+1]=="V":
                        sum+=4
                        i+=2
                    elif s[i+1]=="X":
                        sum+=9
                        i+=2
                    else:
                        sum+=1
                        i+=1
                else:
                        sum+=1
                        i+=1
            elif s[i]=="X":
                if i<len(s)-1:
                    if s[i+1]=="L":
                        sum+=40
                        i+=2
                    elif s[i+1]=="C":
                        sum+=90
                        i+=2
                    else:
                        sum+=10
                        i+=1
                else:
                        sum+=10
                        i+=1
            elif s[i]=="C":
                if i<len(s)-1:
                    if s[i+1]=="D":
                        sum+=400
                        i+=2
                    elif s[i+1]=="M":
                        sum+=900
                        i+=2
                    else:
                        sum+=100
                        i+=1
                else:
                        sum+=100
                        i+=1
            elif s[i]=="V":
                sum+=5
                i+=1
            elif s[i]=="L":
                sum+=50
                i+=1
            elif s[i]=="D":
                sum+=500
                i+=1
            else:
                sum+=1000
                i+=1
        return sum

**ABOUT MY CODE**
Time:- O(n)
Space:- O(1)
Approach:- String, Simulation

        
