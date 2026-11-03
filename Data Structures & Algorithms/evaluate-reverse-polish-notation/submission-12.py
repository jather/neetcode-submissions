class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            print(stack)
            match token:
                case "+":
                    second = stack.pop()
                    stack.append(stack.pop() + second)
                case "-":
                    second = stack.pop()
                    stack.append(stack.pop() - second)
                case "/":
                    second = stack.pop()
                    stack.append(int(stack.pop() / second))
                case "*":
                    second = stack.pop()
                    stack.append(stack.pop() * second)
                case _:
                    stack.append(int(token))
        return stack.pop()