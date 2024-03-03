class CustomStack:

    def __init__(self, maxSize: int):
        self.stack=[]
        self.length=maxSize
        self.top=-1
        
    def push(self, x: int) -> None:
        if self.top<self.length-1:
            self.stack.append(x) 
            self.top=self.top+1
    def pop(self) -> int:
        if self.top!=-1:
            self.top-=1
            return self.stack.pop()
        return -1

    
    def increment(self, k: int, val: int) -> None:
        if k<=self.top+1:
            for i in range(k):
                self.stack[i]+=val
        else:
            for i in range(self.top+1):
                self.stack[i]+=val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)