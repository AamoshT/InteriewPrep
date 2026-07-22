class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        LB, RS = 0,1
        profit = 0
        maxP=0
        while RS < len (prices):
            if prices[LB] < prices[RS]:
                profit = prices[RS] - prices[LB]
                maxP = max(maxP,profit)
            else:
                LB = RS
            RS += 1

                
        return maxP

        