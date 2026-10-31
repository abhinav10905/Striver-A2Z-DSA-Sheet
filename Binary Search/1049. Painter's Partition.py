**QUESTION**
1049. Painter's Partition
You are given A painters and an array C of N integers where C[i] denotes the length of the ith board. Each painter takes B units of time to paint 1 unit of board. You must assign boards to painters such that:
Each painter paints only contiguous segments of boards.
No board can be split between painters.
The goal is to minimize the time to paint all boards.
Return the minimum time required to paint all boards modulo 10000003.

**CONSTRAINTS**
1 <= A <= 1000
1 <= B <= 106
1 <= N <= 105
1 <= C[i] <= 106

**CODE**
class Solution:
    def time(self,C,t):
        c=0
        a=0
        for i in C:
            if a+i<=t:
                a+=i
            else:
                c+=1
                a=i
        if a!=0:
            c+=1
        return c
    def paint(self, A: int, B: int, C: list[int]) -> int:
        low=max(C)
        high=sum(C)
        while low<=high:
            mid=(low+high)//2
            z=self.time(C,mid)
            if z<=A:
                high=mid-1
            elif z>A:
                low=mid+1
        return (low*B)%10000003
        
**ABOUT MY CODE**
Time:- O(n*log(sum(nums)-max(nums)))
Space:- O(1)
Approach:- Binary Search, Recursion
