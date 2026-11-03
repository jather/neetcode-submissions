class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        product = 1
        for num in nums:
            prefix.append(product)
            product *= num
        suffix = [0] * len(nums)
        s = 1
        for i in range(len(nums) - 1, - 1, -1):
            suffix[i] = s
            s *= nums[i]
        result = []
        for i in range(0, len(nums)):
            result.append(prefix[i] * suffix[i])
        return result
