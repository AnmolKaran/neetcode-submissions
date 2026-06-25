class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cts = Counter(tasks)
        heap = []
        for ct in cts:
            heapq.heappush_max(heap,(cts[ct],ct))

        clock = 0
        q = deque()
        
        while heap or q:
            if heap:
                popped = heapq.heappop_max(heap)
                clock +=1
                if popped[0] > 0:
                    remaining_times = popped[0] -1
                timeToAddBack = clock + n
                if remaining_times >0:
                    q.append((remaining_times,popped[1], timeToAddBack))
            else:
                clock+=1
                
                
            
            while q and q[0][2] <= clock:
                heapq.heappush_max(heap,(q[0][0],q[0][1]))
                q.popleft()
        return clock