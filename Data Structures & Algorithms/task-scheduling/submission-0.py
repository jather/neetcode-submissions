import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = [0] * 26
        for task in tasks:
            key = ord(task) - ord("A")
            frequency[key] += 1
        freq_heap = [freq for freq in frequency if freq > 0]
        heapq.heapify_max(freq_heap)
        cooldown = deque()
        cycle = 0
        while freq_heap or cooldown:
            if cooldown and cooldown[0][1] <= cycle:
                cur = cooldown.popleft()
                freq = cur[0]
                if freq > 0:
                    heapq.heappush_max(freq_heap, freq)
            elif freq_heap:
                cur = heapq.heappop_max(freq_heap)
                cur -= 1
                if cur > 0:
                    cooldown.append((cur, cycle + n + 1))
                cycle += 1
            else:
                cycle = cooldown[0][1]

        return cycle
        