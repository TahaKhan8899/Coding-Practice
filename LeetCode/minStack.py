class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, x):
        self.stk.append(x)

    def pop(self):
        self.stk = self.stk[:len(self.stk)-1]

    def top(self):
        return self.stk.pop(len(self.stk)-1)

    def getMin(self):
        tmpStk = [a for a in self.stk]
        tmpStk.sort()
        return tmpStk[0]


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())
