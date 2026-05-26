class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums = set(nums)
        maxlen = 0
        for num in nums:
            if num-1 in setnums:
                continue
            count = 1
            nextnum = num+1
            while nextnum in setnums:
                count +=1
                nextnum +=1
            maxlen = max(maxlen,count)
        return maxlen
            