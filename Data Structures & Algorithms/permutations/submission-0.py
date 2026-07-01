class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        finArr = []
        def dfs(path, seen):    
            if len(path) == len(nums):
                finArr.append(path)
                return

            for i in range(len(nums)):
                if nums[i] in seen:
                    continue
                
                dfs(path +[nums[i]], seen.union({nums[i]}))
        
        dfs([],set())
        return finArr
        