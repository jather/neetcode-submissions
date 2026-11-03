class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(nums, cur, i):
            if len(cur) > len(nums):
                return
            res.append(cur.copy())
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                cur.append(nums[j])
                dfs(nums, cur, j + 1)
                cur.pop()
        dfs(nums, [], 0)
        return res
