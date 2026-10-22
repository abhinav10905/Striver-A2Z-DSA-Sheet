**QUESTION**
750. Upper Bound
Given a sorted array of nums and an integer x, write a program to find the upper bound of x.
The upper bound of x is defined as the smallest index i such that nums[i] > x.
If no such index is found, return the size of the array.

**CONSTRAINTS**
1 <= nums.length <= 105
-105 < nums[i], x < 105
nums is sorted in ascending order.

**CODE**
class Solution:
    def ans(self,low,high,nums,target,z):
        mid=(low+high)//2
        if low>high:
            return z
        if nums[mid]>target:
            z=mid
            high=mid-1
            return self.ans(low,high,nums,target,z)
        else:
            low=mid+1
            return self.ans(low,high,nums,target,z)
    def upperBound(self, nums, x):
        low=0
        high=len(nums)-1
        z=len(nums)
        y=self.ans(low,high,nums,x,z)
        return y
        
**ABOUT MY CODE**
Time:- O(log(n))
Space:- O(1)
Approach:- Binary Search, Recursion
