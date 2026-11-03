class Solution:
    def findMin(self, nums: List[int]) -> int:
        currentMin = nums[0]
        l, r = 1, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < currentMin:
                currentMin = nums[m]
                r = m - 1
            else:
                l = m + 1
        return currentMin
        