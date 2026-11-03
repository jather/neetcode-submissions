class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def recurse(nums, target):
            res = []
            nums_sorted = sorted(nums)
            for i, num in enumerate(nums_sorted):
                if target == num:
                    res.append([num])
                elif target > num:
                    sublists = recurse(nums_sorted[i:], target - num)
                    for sublist in sublists:
                        if sublist:
                            res.append(sublist + [num])
            return res
        return recurse(nums, target)