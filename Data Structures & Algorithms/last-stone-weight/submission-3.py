import heapq 

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        max_heap = stones
        while len(max_heap) > 1:
            x = heapq.heappop_max(max_heap)
            y = heapq.heappop_max(max_heap)
            if x == y:
                continue
            heapq.heappush_max(max_heap, abs(x-y))
            
        if len(max_heap) == 0:
            return 0
        return max_heap[0]

            

        