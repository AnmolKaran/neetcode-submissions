class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        finMap = defaultdict(int)
        for i, v in enumerate(nums):
            if v in finMap:
                return [ finMap[v],i]
            finMap[target-v] = i
        