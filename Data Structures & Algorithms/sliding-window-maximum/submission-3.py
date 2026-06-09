class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q= deque()
        res = []

        for i, v in enumerate(nums):
            print(q)
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            print(q)
            
            q.append(i)
            if q[0]+k <= i:
                q.popleft()
            
            print(q)
            print()


            if i >= k -1:
                res.append(nums[q[0]])
        
        return res
        
            
