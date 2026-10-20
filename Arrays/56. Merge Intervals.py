**QUESTION**
56. Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

**CONSTRAINTS**
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

**CODE**
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        hash={}
        c=0
        for i in intervals:
            if i[0] not in hash:
                hash[i[0]]=1
            else:
                hash[i[0]]+=1
            if i[1] not in hash:
                hash[i[1]]=-1
            else:
                hash[i[1]]-=1
        a=[]
        b=0
        for i in sorted(hash):
            if c==0:
                b=i
            c+=hash[i]
            if c==0:
                a.append([b,i])
        return a

**ABOUT MY CODE**
Time:- O(n*log(n))
Space:- O(n)
Approach:- Array, Sorting
