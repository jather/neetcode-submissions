class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower, upper = 0, len(nums) - 1
        while lower <= upper:
            current = (lower + upper) // 2
            if nums[current] == target:
                return current
            if nums[current] < target:
                lower = current + 1
            else:
                upper = current - 1
        return -1

        