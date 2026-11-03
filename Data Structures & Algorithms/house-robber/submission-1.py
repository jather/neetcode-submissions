class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        recurrence:
        maxMoney[i] = max of (
        maxMoney[i-2] + money[i]
        maxMoney[i-1]
        )

        maxMoney [0] = money[0]
        maxMoney [1] = max(money[0], money[1])
        """
        if len(nums) <= 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], (dp[i-2] + nums[i]))
        
        return dp[-1]
        