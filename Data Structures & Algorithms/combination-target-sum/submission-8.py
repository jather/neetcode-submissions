class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, cur, remaining):
            if remaining == 0:
                res.append(cur.copy())
                return
            for j in range(i, len(nums)):
                if remaining - nums[j] < 0:
                    break
                cur.append(nums[j])
                dfs(j, cur, remaining - nums[j])
                cur.pop()
        dfs(0, [], target)
        return res
