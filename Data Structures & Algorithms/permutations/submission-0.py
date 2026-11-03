class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [0] * len(nums)
        def dfs(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = 1
                dfs(path)
                path.pop()
                used[i] = 0
        dfs([])
        return res
                    
        