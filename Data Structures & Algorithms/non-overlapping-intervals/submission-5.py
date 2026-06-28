class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        arr = sorted(intervals, key = lambda x: x[0])
        removals = 0
        prevEnd = arr[0][1]
        i = 1
        while i < len(arr):
            curr = arr[i]
            if not prevEnd <= curr[0]: 
                if prevEnd <= curr[1]:
                    pass
                else:
                    prevEnd = curr[1]
                removals +=1

            else:
                prevEnd = curr[1]
                

            i+=1
        return removals
        
                