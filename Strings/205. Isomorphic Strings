**QUESTION**
205. Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

**CONSTRAINTS**
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.

**CODE**
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash1={s[0]:t[0]}
        hash2={t[0]:s[0]}
        for i in range (1,len(s)):
            if s[i] in hash1:
                if hash1[s[i]]!=t[i]:
                    return False
            else:
                hash1[s[i]]=t[i]
            if t[i] in hash2:
                if hash2[t[i]]!=s[i]:
                    return False
            else:
                hash2[t[i]]=s[i]
        return True
        
**ABOUT MY CODE**
Time:- O(n)
Space:- O(n)
Approach:- Hash Table
