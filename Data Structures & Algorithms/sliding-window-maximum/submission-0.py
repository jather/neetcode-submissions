from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = deque() #(position, value)
        l = 0
        for r in range(len(nums)):
            while len(window) > 0 and window[-1][1] < nums[r]:
                window.pop()
            window.append((r, nums[r]))
            if r - l + 1 == k:
                res.append(window[0][1])
                if window[0][0] == l:
                    window.popleft()
                l += 1
        return res

