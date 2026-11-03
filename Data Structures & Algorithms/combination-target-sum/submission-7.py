class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums_sorted = sorted(nums)
        def recurse(nums, target):
            res = []
            for i, num in enumerate(nums):
                if target == num:
                    res.append([num])
                    break
                elif target > num:
                    sublists = recurse(nums[i:], target - num)
                    for sublist in sublists:
                        if sublist:
                            res.append(sublist + [num])
            return res
        return recurse(nums_sorted, target)