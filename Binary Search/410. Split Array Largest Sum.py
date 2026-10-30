**QUESTION**
410. Split Array Largest Sum
Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.
Return the minimized largest sum of the split.
A subarray is a contiguous part of the array.

**CONSTRAINTS**
1 <= nums.length <= 1000
0 <= nums[i] <= 106
1 <= k <= min(50, nums.length)

**CODE**
class Solution:
    def time(self,nums,t):
        c=0
        a=0
        for i in nums:
            if a+i<=t:
                a+=i
            else:
                c+=1
                a=i
        if a!=0:
            c+=1
        return c
    def splitArray(self, nums: list[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)
        while low<=high:
            mid=(low+high)//2
            z=self.time(nums,mid)
            if z<=k:
                high=mid-1
            elif z>k:
                low=mid+1
        return low
        
