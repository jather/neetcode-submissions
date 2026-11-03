class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sNums = sorted(nums)
        result = []
        for i, num in enumerate(sNums):
            if num > 0:
                break
            if i > 0 and sNums[i] == sNums[i-1]:
                continue
            j = i + 1
            k = len(sNums) - 1
            while j < k:
                if sNums[j] + sNums[k] + num == 0:
                    result.append([sNums[j], sNums[k], num])
                    j += 1
                    while sNums[j] == sNums[j-1] and j < k:
                        j += 1
                elif j < k and sNums[j] + sNums[k] + num < 0:
                    j += 1
                else:
                    k -= 1
        return result


        