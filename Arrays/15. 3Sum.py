**QUESTION**
15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

**CONSTRAINTS**
3 <= nums.length <= 3000
-105 <= nums[i] <= 105

**CODE**
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        a=[]
        nums.sort()
        for i in range (0,len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                z=nums[i]+nums[j]+nums[k]
                if z>0:
                    k-=1
                elif z<0:
                    j+=1
                else:
                    b=[nums[i],nums[j],nums[k]]
                    a.append(b)
                    j+=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
        return a

**ABOUT MY CODE**
Time:- O(n**2)
Space:- O(n)
Approach:- Sorting
