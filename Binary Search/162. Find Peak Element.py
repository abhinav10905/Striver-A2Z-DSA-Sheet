**QUESTION**
162. Find Peak Element
A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
You must write an algorithm that runs in O(log n) time.

**CONSTRAINTS**
1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.

**CODE**
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        while low<high:
            mid=(low+high)//2
            if nums[mid]>nums[mid+1]:
                high=mid
            else:
                low=mid+1
        return low
                
**ABOUT MY CODE**
Time:- O(logn)
Space:- O(1)
Approach:- Binary Search
        
