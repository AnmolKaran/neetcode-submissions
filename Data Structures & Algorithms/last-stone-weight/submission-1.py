class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            top = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)
            if top == second:
                continue
            heapq.heappush_max(stones, top-second)
        if stones:
            return stones[0]
        else:
            return 0