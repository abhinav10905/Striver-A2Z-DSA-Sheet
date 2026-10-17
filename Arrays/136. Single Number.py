**QUESTION**
136. Single Number
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

**CONSTRAINTS**
1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.

**CODE**
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=0
        for i in nums:
            a=a^i
        return a

**ABOUT MY CODE**
Time:- O(n)
Space:- O(1)
Approach:- XOR Approach
