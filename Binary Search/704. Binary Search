**QUESTION**
704. Binary Search
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

**CONSTRAINTS**
1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.

**CODE**
class Solution:
    def ans(self,low,high,nums,target):
        if low>high:
            return -1
        mid=(low+high)//2
        if target<nums[mid]:
            low=low
            high=mid-1
            return self.ans(low,high,nums,target)
        elif target>nums[mid]:
            low=mid+1
            high=high
            return self.ans(low,high,nums,target)
        else:
            return mid
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        return self.ans(low,high,nums,target)

**ABOUT MY CODE**
Time:- O(logn)
Space:- O(1)
Approach:- Binary Search
