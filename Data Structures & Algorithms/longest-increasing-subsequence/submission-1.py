class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [0 for _ in range(len(nums))]
        LIS[0] = 1
        for k in range(1, len(nums)):
            LIS[k] = 1 + max([0]+[LIS[i] for i in range(len(LIS)) if i <k and nums[i] < nums[k]])
        
        return max(LIS)

