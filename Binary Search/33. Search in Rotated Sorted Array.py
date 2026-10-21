**QUESTION**
33. Search in Rotated Sorted Array
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

**CONSTRAINTS**
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104

**CODE**
class Solution:
    def ans(self,low,high,nums,target):
        if low>high:
            return -1
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>=nums[low]:
            if target<nums[mid] and target>=nums[low]:
                high=mid-1
                return self.ans(low,high,nums,target)
            else:
                low=mid+1
                return self.ans(low,high,nums,target)
        else:
            if target>nums[mid] and target<=nums[high]:
                low=mid+1
                return self.ans(low,high,nums,target)
            else:
                high=mid-1
                return self.ans(low,high,nums,target)
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        return self.ans(low,high,nums,target)

**ABOUT MY CODE**
Time:- O(logn)
Space:- O(1)
Approach:- Binary Search, Recursion
