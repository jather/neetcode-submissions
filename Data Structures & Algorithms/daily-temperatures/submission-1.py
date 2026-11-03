class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # pair (temperature, index)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                _, stackI = stack.pop()
                result[stackI] = i - stackI
            stack.append((t, i))
        return result
