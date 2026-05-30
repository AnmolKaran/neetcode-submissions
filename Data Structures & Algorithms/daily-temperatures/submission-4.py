class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dp = [0] * len(temperatures)
        dp[-1] = 0
        for i in range(len(dp)-2,-1,-1):
            j = i+1
            while j < len(dp) and temperatures[j] <= temperatures[i]:
                if dp[j] == 0:
                    dp[i] == 0
                    break
                j = j +dp[j]
            
            if j < len(dp) and temperatures[j] > temperatures[i]:
                dp[i]= j-i
        return dp



