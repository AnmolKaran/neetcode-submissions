class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftpass = []
        countingprod = 1
        for n in nums:
            leftpass.append(countingprod)
            countingprod*=n
            
        rightpass = [0 for i in range(len(nums))]
        rightcountingprod = 1
        for i in range(len(nums)-1,-1,-1):
            rightpass[i] = rightcountingprod
            rightcountingprod *=nums[i]
        
        res = [0 for i in range(len(nums))]
        for i, v in enumerate(res):
            res[i] = leftpass[i] * rightpass[i]
        
        return res