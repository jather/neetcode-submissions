class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        potential = {}
        for i in range(0, len(nums)):
            if nums[i] in potential:
                return [potential[nums[i]], i]
            potential[target - nums[i]] = i