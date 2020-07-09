from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #first move must be buy
        #last move must be sell
        
        #find max diff between buy and sell prices
        #iterate through buy, sell
        max_profit = 0
        for b in range(0,len(prices)):
            for s in range(b+1,len(prices)):
                profit = prices[s] - prices[b]
                if profit > max_profit:
                    max_profit = profit
        return max_profit

s = Solution()
assert s.maxProfit(prices=[7,6,4,3,1])==0
assert s.maxProfit(prices=[7,1,5,3,6,4])==5