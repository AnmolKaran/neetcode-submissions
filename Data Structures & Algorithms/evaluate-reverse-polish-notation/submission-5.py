class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in "+-*/":
                second = int(stack.pop())
                first = int(stack.pop())
                print(first,second,t)
                if t == "+":
                    stack.append(first+second)
                elif t == "-":
                    stack.append(first-second)
                elif t == "*":
                    stack.append(first*second)
                elif t == "/":
                    stack.append(first/second)
            else:
                stack.append(int(t))
        return int(stack[0])