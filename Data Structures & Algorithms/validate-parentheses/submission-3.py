class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openers = "({["
        closers = ")}]"
        for c in s:
            if c in openers:
                stack.append(c)
            elif c in closers:
                if not stack: return False
                popped = stack.pop()
                if popped not in openers:
                    return False

                if openers.index(popped) != closers.index(c):
                    return False
        if not stack:
            return True
        return False