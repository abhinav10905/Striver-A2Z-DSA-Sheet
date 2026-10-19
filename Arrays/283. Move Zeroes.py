**QUESTION**
283. Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

**CONSTRAINTS**
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

**CODE**
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=0
        for i in range (0,len(nums)):
            if nums[i]!=0:
                nums[i],nums[k]=nums[k],nums[i]
                k+=1

**ABOUT MY CODE**
Time:- O(n)
Space:- O(1)
Approach:- Two Pointers, Swapping
