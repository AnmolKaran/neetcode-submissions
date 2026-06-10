class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(1,len(nums)+1):
            v = abs(nums[i-1])
            if nums[v-1] < 0:
                return abs(v)
            nums[abs(v-1)] *=-1
