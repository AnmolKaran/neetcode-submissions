
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        window = deque()
        window.append(nums[0])
        runningSum = nums[0]
        counter = 1
        best = nums[0]
        while counter < len(nums):
            if runningSum <0:
                window = deque()
                
                runningSum = 0
            runningSum += nums[counter]
            window.append(nums[0])
            if runningSum > best:
                best = runningSum
            
            counter +=1
        return best
