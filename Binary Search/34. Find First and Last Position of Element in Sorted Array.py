**QUESTION**
34. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

**CONSTRAINTS**
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

**CODE**
class Solution:
    def l_ans(self,low,high,nums,target,z):
        mid=(low+high)//2
        if low>high:
            return z
        if nums[mid]>=target:
            z=mid
            high=mid-1
            return self.l_ans(low,high,nums,target,z)
        else:
            low=mid+1
            return self.l_ans(low,high,nums,target,z)
        return z
    def u_ans(self,low,high,nums,target,z):
        mid=(low+high)//2
        if low>high:
            return z
        if nums[mid]>target:
            z=mid
            high=mid-1
            return self.u_ans(low,high,nums,target,z)
        else:
            low=mid+1
            return self.u_ans(low,high,nums,target,z)
        return z
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        z=-1
        low=0
        high=len(nums)-1
        lower_bound=self.l_ans(low,high,nums,target,z)
        low=0
        high=len(nums)-1
        z=-1
        upper_bound=self.u_ans(low,high,nums,target,z)
        if upper_bound==-1:
            upper_bound=len(nums)-1
        else:
            upper_bound-=1
        if len(nums)==0:
            return [-1,-1]
        elif target>nums[-1]:
            return [-1,-1]
        elif nums[lower_bound]!=target:
            return [-1,-1]
        else:
            return [lower_bound,upper_bound]

**ABOUT MY CODE**
Time:- O(logn)
Space:- O(1)
Approach:- Binary Search
