class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.small=[float('inf')]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val<=self.small[-1]:
            self.small.append(val)
        self.stack.append(val)
    def pop(self):
        """
        :rtype: None
        """
        p=self.stack.pop()
        if p==self.small[-1]:
            self.small.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.small[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()