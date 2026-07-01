class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        fin = []
        nums = sorted(nums)
        def helper(ind,path):
            
            if ind>= len(nums):
                fin.append(path)
                return
            
            

            helper(ind+1,path + [nums[ind]])

            while ind +1< len(nums) and nums[ind+1] == nums[ind]:
                ind+=1
            helper(ind+1,path)  
            
        helper(0,[])
        return fin