class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        arr = sorted(intervals, key = lambda x: x[0])
        ind = 0
        n = len(arr)
        res = [arr[0]]
        if n == 1:
            return arr
        while ind < n-1:
            compareWith = arr[ind+1]
            #curr = intervals[ind]
            curr = res[-1]
            if curr[1] >= compareWith[0]:
                if res:
                    res.pop()
                #print(curr,compareWith)
                res.append([min(curr[0],compareWith[0]) ,max(curr[1],compareWith[1] )])
            else:
                res.append(compareWith)
            ind+=1
                
        return res

