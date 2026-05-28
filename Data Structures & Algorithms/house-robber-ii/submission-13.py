class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

            
        dp = [0 for _ in range(len(nums))]
        

        dp[1] = nums[1]
        dp[0] = dp[1] -1
        firsthouse = 0 
        lasthouse = 0
        
        dp[2] = max(nums[1],nums[2])
        for i in range(3,len(nums)):
            dp[i]= max(dp[i-2] + nums[i],dp[i-1])
        lasthouse =  dp[-1]
        print(dp)


        dp = [0 for i in range(len(nums)-1)]
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)-1):
            dp[i]= max(dp[i-2] + nums[i],dp[i-1])
        
        firsthouse = dp[-1]
        print(firsthouse,lasthouse)
        return max(firsthouse,lasthouse)