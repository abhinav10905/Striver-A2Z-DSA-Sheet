**QUESTION**
Leaders in an Array
Given an integer array nums, return a list of all the leaders in the array.
A leader in an array is an element whose value is strictly greater than all elements to its right in the given array. The rightmost element is always a leader. The elements in the leader array must appear in the order they appear in the nums array.

**CONSTRAINTS**
1 <= nums.length <= 105
-104 <= nums[i] <= 104

**CODE**
class Solution:
    def leaders(self, nums):
        nums=nums[::-1]
        a=[nums[0]]
        m=nums[0]
        for i in nums:
            if i>m:
                a.append(i)
                m=i
        return a[::-1]

**ABOUT MY CODE**
Time:- O(n)
Space:- O(n)
Approach:- Array, Reversing
