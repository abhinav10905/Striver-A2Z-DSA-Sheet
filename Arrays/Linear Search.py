**QUESTION**
Linear Search
Given an array of integers nums and an integer target, find the smallest index (0 based indexing) where the target appears in the array. If the target is not found in the array, return -1

**CONSTRAINTS***
1 <= nums.length <= 105
-104 <= nums[i] <= 104
-104 <= target <= 104

**CODE**
class Solution:
    def linearSearch(self, nums, target):
        a=-1
        i=0
        while i<len(nums):
            if nums[i]==target:
                a=i
                break
            i+=1
        return a
    
**ABOUT MY CODE**
Time:- O(n)
Space:- O(1)
Approach:- Array
