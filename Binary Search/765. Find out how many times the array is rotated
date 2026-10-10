**QUESTION**
765. Find out how many times the array is rotated
Given an integer array nums of size n, sorted in ascending order with distinct values. The array has been right rotated an unknown number of times, between 0 and n-1 (including). Determine the number of rotations performed on the array.

**CONSTRAINTS**
n == nums.length
1 <= n <= 104
-104 <= nums[i] <= 104
All the integers of nums are unique.

**CODE**
class Solution:
    def ans(self,nums,low,high):
        if low>high:
            return 0
        mid=(low+high)//2
        if nums[mid]<nums[mid-1]:
            return mid
        elif nums[mid]>=nums[0]:
            low=mid+1
            return self.ans(nums,low,high)
        else:
            high=mid-1
            return self.ans(nums,low,high)
    def findKRotation(self, nums):
        low=0
        high=len(nums)-1
        z=-1
        z=self.ans(nums,low,high)
        return z

**ABOUT MY CODE**
Time:- O(log(n))
Space:- O(1)
Approach:- Binary Search, Recursion
