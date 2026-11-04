import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums
        heapq.heapify_max(heap)
        res = 0
        for _ in range(k):
            res = heapq.heappop_max(heap)
        return res

        