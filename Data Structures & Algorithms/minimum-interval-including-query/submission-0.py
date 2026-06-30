class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        arr = sorted(intervals, key = lambda x: x[0])
        sorted_queries = sorted(queries)
        arrInd = 0
        heap = []
        res_map = {}
        for query in sorted_queries:
            while arrInd < len(arr) and arr[arrInd][0] <= query:
                heapq.heappush(heap,(arr[arrInd][1]-arr[arrInd][0]+1,arr[arrInd][1] ))
                arrInd +=1
            while heap and heap[0][1] <query:
                heapq.heappop(heap)
            if heap:
                res_map[query] = heap[0][0]
            else:
                res_map[query] =-1
        return [res_map[q] for q in queries]
