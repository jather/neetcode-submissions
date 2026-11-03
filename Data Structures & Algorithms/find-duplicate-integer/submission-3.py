import math
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast is slow:
                break
        
        s2 = 0
        while slow is not s2:
            slow = nums[slow]
            s2 = nums[s2]
        
        return slow
