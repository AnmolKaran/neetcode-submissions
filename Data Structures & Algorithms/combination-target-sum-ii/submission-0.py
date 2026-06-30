class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        i = 0
        arr = []
        while i < len(nums) and nums[i]<= target:
            arr.append(nums[i])
            i+=1
        
        finArr = []
        def dfs(startInd,path, currsum):
            if currsum == target:
                finArr.append(path)
                return
            if currsum > target:
                return
            
            for i in range(startInd,len(arr)):
                if i > startInd and arr[i] == arr[i-1]:
                    continue
                dfs(i+1,path + [arr[i]], currsum + arr[i])

        dfs(0,[],0)

        return finArr