**QUESTION**
42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

**CONSTRAINTS**
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

**CODE**
class Solution:
    def trap(self, height: List[int]) -> int:
        c=0
        i=0
        j=len(height)-1
        l_max=height[i]
        r_max=height[j]
        while i<j:
            if height[i]<height[j]:
                i+=1
                l_max=max(l_max,height[i])
                c+=(l_max-height[i])
            else:
                j-=1
                r_max=max(r_max,height[j])
                c+=(r_max-height[j])
        return c
        
**ABOUT MY CODE**
Time:- O(n)
Space:- O(1)
Approach:- Two Pointers, Array
