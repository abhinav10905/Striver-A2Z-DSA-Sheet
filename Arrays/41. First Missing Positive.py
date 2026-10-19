**QUESTION**
41. First Missing Positive
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

**CONSTRAINTS**
1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1

**CODE**
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range (0,len(nums)):
            while 1<=nums[i]<=len(nums) and nums[nums[i]-1]!=nums[i]:
                a=nums[i]-1
                nums[i],nums[a]=nums[a],nums[i]
        for i in range (0,len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1
        
**ABOUT MY CODE**
Time:- O(n)
Space:- O(1)
Approach:- Math, Array
