**QUESTION**
229. Majority Element II
Given an integer array of size n, find all elements that appear more than ⌊n / 3⌋ times.

**CONSTRAINTS**
1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109

**CODE**
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        hash={}
        hash[nums[0]]=1
        for i in range (1,n):
            if nums[i] in hash:
                hash[nums[i]]+=1
            else:
                hash[nums[i]]=1
        c=[]
        ans=n//3
        for i in hash:
            if hash[i]>ans:
                c=c+[i]
        return c

**ABOUT MY CODE**
Time:- O(n)
Space:- O(n)
Approach:- Hash Map
