**QUESTION**
1011. Capacity To Ship Packages Within D Days
A conveyor belt has packages that must be shipped from one port to another within days days.
The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

**CONSTRAINTS**
1 <= days <= weights.length <= 5 * 104
1 <= weights[i] <= 500

**CODE**
class Solution:
    def time(self,weights,t):
        c=1
        d=0
        for i in range (0,len(weights)):
            d+=weights[i]
            if d>t:
                c+=1
                d=weights[i]
        return c
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        ans=-1
        while low<=high:
            mid=(low+high)//2
            z=self.time(weights,mid)
            if z>days:
                low=mid+1
            else:
                ans=mid
                high=mid-1
        return ans
        
**ABOUT MY CODE**
Time:- O(n*log(sum(weights)))
Space:- O(1)
Approach:- Binary Search, Recursion       
