class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        lowestPriceSoFar = prices[0]
        #bestProfitSoFar = 0
        for i, v in enumerate(prices):
            lowestPriceSoFar = min(v,lowestPriceSoFar)
            profit = v -lowestPriceSoFar
            if i >0:
                dp[i] = max(dp[i-1],profit)
            else:
                dp[i] = max(0,profit)
            
        return dp[-1]
