class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ind = 0
        res= []
        while ind < len(intervals):
            if intervals[ind][1] < newInterval[0]:
                res.append(intervals[ind])
                ind +=1
                
                
            else:
                break

        while ind < len(intervals):
            if intervals[ind][0] <= newInterval[1]:
                newInterval[0] = min(newInterval[0], intervals[ind][0])
                newInterval[1] = max(newInterval[1], intervals[ind][1])
                ind +=1
            else:
                break
        

        print(res)
        res.append(newInterval)
        res.extend(intervals[ind:])
        return res

            
        
        