class Solution:
    def isValid(self, s: str) -> bool:
        openBrackets = ["(", "{", "["]
        closeBrackets = [")", "}", "]"]
        stack = []
        for char in s:
            if char not in openBrackets and char not in closeBrackets:
                continue
            if char in openBrackets:
                stack.append(closeBrackets[openBrackets.index(char)])
            if char in closeBrackets:
                if len(stack) <= 0:
                    return False
                if char != stack.pop():
                    return False
        if len(stack) != 0:
            return False
        return True

            