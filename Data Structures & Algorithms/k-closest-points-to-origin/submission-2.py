class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [(math.sqrt(v[0]**2+v[1]**2), i) for i, v in enumerate(points)]
        heapq.heapify(dists)
        fin = []
        for ct in range(k):   
            
            fin .append(points[heapq.heappop(dists)[1]])

        return fin