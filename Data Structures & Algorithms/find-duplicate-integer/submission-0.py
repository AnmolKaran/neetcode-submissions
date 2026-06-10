class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for i , v in enumerate(nums):
            if v in seen:
                return v
            else:
                seen.add(v)
        return None