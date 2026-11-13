**QUESTION**
138. Find the repeating and missing number
Given an integer array nums of size n containing values from [1, n] and each value appears exactly once in the array, except for A, which appears twice and B which is missing.
Return the values A and B, as an array of size 2, where A appears in the 0-th index and B in the 1st index.
Note: You are not allowed to modify the original array.

**CONSTRAINTS**
n == nums.length
1 <= n <= 105
n - 2 elements in nums appear exactly once and are valued between [1, n].
1 element in nums appears twice, and is valued between [1, n].

**CODE**
class Solution:
    def findMissingRepeatingNumbers(self, nums):
        hash=[0]*n
        for i in nums:
            hash[i-1]+=1
        a=0
        b=0
        for i in range (0,n):
            if hash[i]==0:
                b=i+1
            elif hash[i]==2:
                a=i+1
        return [a,b]
