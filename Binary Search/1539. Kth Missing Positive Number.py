**QUESTION**
1539. Kth Missing Positive Number
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
Return the kth positive integer that is missing from this array.

**CONSTRAINTS**
1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length

**FOLLOW UP**
Could you solve this problem in less than O(n) complexity?

**CODE**
class Solution:
    def ans(self,mid,arr):
        a=arr[mid]-(mid+1)
        return a
    def findKthPositive(self, arr: list[int], k: int) -> int:
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            b=self.ans(mid,arr)
            if b<k:
                low=mid+1
            else:
                high=mid-1
        return low+k

**ABOUT MY CODE**
Time:- O(log(len(arr))
Space:- O(1)
Approach:- Binary Search, Recursion
