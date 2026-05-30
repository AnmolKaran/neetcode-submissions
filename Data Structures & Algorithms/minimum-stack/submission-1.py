class MinStack:

    def __init__(self):
        self.stack = []
        self.minElem = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minElem == None or val < self.minElem :
            self.minElem = val

    def pop(self) -> None:
        popped = self.stack.pop()
        if self.stack and popped == self.minElem:
            self.minElem = min(self.stack)
        elif popped == self.minElem: 
            self.minElem =None
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minElem
