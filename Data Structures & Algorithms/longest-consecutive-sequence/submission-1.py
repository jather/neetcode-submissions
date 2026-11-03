class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max = 0
        current = 1

        for num in nums:
            if num-1 in numSet:
                continue
            i = num + 1
            while i in numSet:
                current += 1
                i += 1
            if current > max:
                max = current
            current = 1
        return max