**QUESTION**
Second Largest Element
Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.

**CONSTRAINTS**
1 <= nums.length <= 105
-104 <= nums[i] <= 104
nums may contain duplicate elements.

**CODE**
class Solution:
    def secondLargestElement(self, nums):
        a=nums[0]
        b=-1
        for i in range (1,len(nums)):
            if nums[i]>a:
                b=a
                a=nums[i]
            elif nums[i]==a:
                pass
            elif nums[i]>b:
                b=nums[i]
        return b

**ABOUT MY CODE**
Time:- O(n)
Space:- O(1)
Approach:- Math, Array
