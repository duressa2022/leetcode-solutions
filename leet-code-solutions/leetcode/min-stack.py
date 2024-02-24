class MinStack:
    #This code provide the brutefoce methos of min stack implementation
    def __init__(self):
        self.normalStack=[]
        self.minStack=[]

    def push(self, val: int) -> None:
        self.normalStack.append(val)
        if len(self.minStack)==0 or  val<=self.minStack[-1]:
            self.minStack.append(val)
  
    def pop(self) -> None:
        temp=self.normalStack.pop()
        if self.minStack and temp==self.minStack[-1]:
            self.minStack.pop()
        
    def top(self) -> int:
        return self.normalStack[-1]
        
    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()