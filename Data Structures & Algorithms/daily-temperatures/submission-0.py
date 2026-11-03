class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range(0, len(temperatures)):
            if not stack:
                stack.append((temperatures[i], i))
            elif temperatures[i] < stack[-1][0]:
                stack.append((temperatures[i], i))
            else:
                while stack and temperatures[i] > stack[-1][0]:
                    lesser = stack.pop()
                    lesserIndex = lesser[1]
                    result[lesserIndex] = i - lesserIndex
                stack.append((temperatures[i], i))
        return result
