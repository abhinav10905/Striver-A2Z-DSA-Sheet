**QUESTION**
154. Book Allocation Problem
Given an array nums of n integers, where nums[i] represents the number of pages in the i-th book, and an integer m representing the number of students, allocate all the books to the students so that each student gets at least one book, each book is allocated to only one student, and the allocation is contiguous.
Allocate the books to m students in such a way that the maximum number of pages assigned to a student is minimized. If the allocation of books is not possible, return -1.

**CONSTRAINTS**
1 <= n, m <= 104
1 <= nums[i] <= 105

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
    def findPages(self, nums, m):
        if len(nums)<m:
            return -1
        low=max(nums)
        high=sum(nums)
        while low<=high:
            mid=(low+high)//2
            z=self.time(nums,mid)
            if z<=m:
                high=mid-1
            elif z>m:
                low=mid+1
        return low
        
**ABOUT MY CODE**
Time:- O(n*log(sum(nums)-max(nums)))
Space:- O(1)
Approach:- Binary Search, Recursion
