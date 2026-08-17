**QUESTION**
121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

**CONSTRAINTS**
1 <= prices.length <= 105
0 <= prices[i] <= 104

**CODE**
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=prices[0]
        sum=0
        for i in range (1,len(prices)):
            b=prices[i]
            a=b-m
            sum=max(sum,a)
            m=min(m,b)
        return sum

**ABOUT MY CODE**
Time:- O(n)
Space:- O(1)
Approach:- Greedy
