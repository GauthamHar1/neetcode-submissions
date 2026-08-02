class MinStack:
    # ok so we want a stack that keeps track of
    # the current min at every position

    def __init__(self):
        self.minstack = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        elif self.minstack and val <= self.minstack[-1]:
            self.minstack.append(val)
        

    def pop(self) -> None:
        if self.minstack[-1] == self.stack.pop():
            self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        
