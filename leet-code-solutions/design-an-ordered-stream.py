class OrderedStream:

    def __init__(self, n: int):
        self.array=[None]*(n)
        self.i=0
    def insert(self, idKey: int, value: str) -> List[str]:
        self.array[idKey-1]=value
        result=[]
        while self.i<len(self.array) and self.array[self.i]!=None:
            result.append(self.array[self.i])
            self.i+=1
        return result
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)