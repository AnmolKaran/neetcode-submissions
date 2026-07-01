class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [{""}]
        for i in range(1,n+1):
            prevSet = dp[i-1]
            currSet = set()
            for s in prevSet:
                for i in range(len(s)):
                    currSet.add("(" + s[:i] + ")" + s[i:])
                currSet.add("(" + s + ")")
                currSet.add("()" + s)
                currSet.add( s + "()")
            dp.append(currSet)
        return list(dp[-1])


                
        
