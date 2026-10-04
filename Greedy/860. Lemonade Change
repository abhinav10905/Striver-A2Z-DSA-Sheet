**QUESTION**
860. Lemonade Change
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
Note that you do not have any change in hand at first.
Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

**CONSTRAINTS**
1 <= bills.length <= 105
bills[i] is either 5, 10, or 20.

**CODE**
class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        a=[0,0,0]
        for i in bills:
            if i==5:
                a[0]+=1
            elif i==10:
                a[1]+=1
                if a[0]==0:
                    return False
                a[0]-=1
            else:
                a[2]+=1
                if a[0]==0:
                    return False
                elif a[1]==0:
                    if a[0]<=2:
                        return False
                    else:
                        a[0]-=3
                else:
                    a[0]-=1
                    a[1]-=1
        return True

**ABOUT MY CODE**
Time:- O(n)
Space:- O(1)
Approach:- Greedy
