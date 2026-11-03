class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        res = 0
        dpTable = [0] * n
        dpTable[0] = 1
        dpTable[1] = 2
        for i in range(2, n):
            dpTable[i] = dpTable[i-1] + dpTable[i-2]
        return dpTable[n - 1]

        