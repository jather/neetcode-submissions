import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for point in points:
            distance = point[0]**2 + point[1]**2
            heapq.heappush_max(maxHeap, (distance, point[0], point[1]))
            if len(maxHeap) > k:
                heapq.heappop_max(maxHeap)
        
        res = []
        for point in maxHeap:
            distance, x, y = point[0], point[1], point[2]
            res.append([x, y])
        
        return res
        


