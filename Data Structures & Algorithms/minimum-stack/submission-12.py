class MinStack:
    # we need to keep track of the elements in a sorted order
    # how do we do this O(1) 
    # like when we add it somehow needs to be in an order but then everytime
    # we add something how do we not have to shift everything else?
    # then maybe im thinking about it wrong, is there a way to do this 
    # without keeping track of the whole order? 

    # what if we just have a normal list and we use that to keep track
    # of the mins, every time a new number gets added,
    def __init__(self):
        self.stack = []
        self.tracker = []
        

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.tracker)==0:
            self.tracker.append(val)
        else:
            self.tracker.append(min(val,self.tracker[-1]))
       

        

    def pop(self) -> None:
        old = self.stack.pop()
        if old not in self.stack:
            while self.tracker and old==self.tracker[-1]:
                self.tracker.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        
    # for get min if we want it to be O(1) we need to keep
    # track of the min as we are adding, in another var
    def getMin(self) -> int:
        if self.tracker:
            return self.tracker[-1]
        else:
            return -1000

