class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        minSize = 0
        currSum = nums[0]
        r = 0
        while r < len(nums):
            while currSum < target:
                r+=1
                if r >=len(nums):
                    return minSize
                currSum +=nums[r]
                
                

                
            if minSize !=0 :
                minSize = min(r-l+1,minSize)
            else: 
                minSize = r-l+1

            currSum -= nums[l]
            l+=1
        return minSize
            
