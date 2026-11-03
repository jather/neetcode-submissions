class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.recurse(nums, target)
    def recurse(self, nums, target):
        res = []

        for i, num in enumerate(nums):
            if target == num:
                res.append([num])
            if target < 0:
                continue
            sublists = self.recurse(nums[i:], target - num)
            for sublist in sublists:
                if sublist:
                    res.append(sublist + [num])
        return res
        
        
        
        