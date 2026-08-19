**QUESTION**
485. Max Consecutive Ones
Given a binary array nums, return the maximum number of consecutive 1's in the array.

**CONSTRAINTS**
1 <= nums.length <= 105
nums[i] is either 0 or 1.

**CODE**
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        d=0
        for i in nums:
            if i==1:
                c+=1
            else:
                d=max(d,c)
                c=0
        d=max(c,d)
        return d
        
**ABOUT MY CODE**
Time:- O(n)
Space:- O(1)
Approach:- Counting, Maximum Value
