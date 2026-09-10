**QUESTION**
88. Merge Sorted Array
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

**CONSTRAINTS**
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109

**CODE**
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=m-1
        j=n-1
        r=m+n-1
        while i>=0 or j>=0:
            if j>=0 and i!=-1 and nums2[j]>nums1[i]:
                nums1[r]=nums2[j]
                j-=1
            elif i==-1:
                nums1[r]=nums2[j]
                j-=1
            else:
                nums1[r]=nums1[i]
                i-=1
            r-=1

**ABOUT MY CODE**
Time:- O(m+n)
Space:- O(1)
Approach:- Two Pointers, Array
