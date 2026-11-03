class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1:
            return nums[0]
        first = self.rob_dp(nums[:len(nums)-1])
        second = self.rob_dp(nums[1:])
        return max(first, second)
    
    def rob_dp(self, nums):
        pprev, prev = 0, 0
        for num in nums:
            tmp = max(pprev + num, prev)
            pprev = prev
            prev = tmp
        return prev

        