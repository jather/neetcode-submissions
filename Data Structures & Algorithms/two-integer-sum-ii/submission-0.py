class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        last = len(numbers) - 1
        first = 0
        while last > first:
            if numbers[first] + numbers[last] == target:
                return [first + 1, last + 1]
            if numbers[first] + numbers[last] < target:
                first += 1
            elif numbers[first] + numbers[last] > target:
                last -= 1

