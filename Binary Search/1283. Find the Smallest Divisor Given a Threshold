**QUESTION**
1283. Find the Smallest Divisor Given a Threshold
Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.
Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).
The test cases are generated so that there will be an answer.

**CONSTRAINTS**
1 <= nums.length <= 5 * 104
1 <= nums[i] <= 106
nums.length <= threshold <= 106

**CODE**
class Solution:
    def time(self,nums,t):
        c=0
        for i in range (0,len(nums)):
            c+=ceil(nums[i]/t)
        return c
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        low=1
        high=max(nums)
        ans=0
        while low<=high:
            mid=(low+high)//2
            z=self.time(nums,mid)
            if z>threshold:
                ans=mid
                low=mid+1
            elif z==threshold:
                ans=mid
                high=mid-1
            else:
                high=mid-1
        return low

**ABOUT MY CODE**
Time:- O(n*log(max(nums)))
Space:- O(1)
Approach:- Binary Search, Recursion
