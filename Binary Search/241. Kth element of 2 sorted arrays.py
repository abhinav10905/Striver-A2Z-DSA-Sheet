**QUESTION**
241. Kth element of 2 sorted arrays
Given two sorted arrays a and b of size m and n respectively. Find the kth element of the final sorted array.

**CONSTRAINTS**
1 <= m, n <= 104
0 <= arr1[i[, arr2[i] < 109
1 <= k <= m+n

**CODE**
class Solution:
    def kthElement(self, a, b, k):
        m=len(a)
        n=len(b)
        hash=[0]*(m+n)
        i=0
        j=0
        z=0
        while i<m and j<n:
            if a[i]<b[j]:
                hash[z]=a[i]
                i+=1
            else:
                hash[z]=b[j]
                j+=1
            z+=1
        while i<m:
            hash[z]=a[i]
            i+=1
            z+=1
        while j<n:
            hash[z]=b[j]
            j+=1
            z+=1
        return hash[k-1]

**ABOUT MY CODE**
Time:- O(log(m+n))
Space:- O(1)
Approach:- Binary Search       
