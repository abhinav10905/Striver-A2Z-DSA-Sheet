**QUESTION**
189. Rotate Array
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

**CONSTRAINTS**
1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

**CODE**
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a=len(nums)
        k=k%a
        nums[:a-k]=nums[:a-k][::-1]
        nums[a-k:]=nums[a-k:][::-1]
        nums[::]=nums[::-1]

**ABOUT MY CODE**
Time:- O(n)
Space:- O(n)
Approach:- Reversing
