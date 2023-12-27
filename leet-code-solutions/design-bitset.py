class Bitset:

    def __init__(self, size: int):
        self.bitSet=[str(0) for i in range(size)]
        self.image=[str(1) for i in range(size)]
        self.number_of_zero=size
        self.number_of_ones=0
    def fix(self, idx: int) -> None:
        if self.bitSet[idx]==str(0):
            self.number_of_zero-=1
            self.number_of_ones+=1
        self.bitSet[idx]=str(1)
        self.image[idx]=str(0)
    def unfix(self, idx: int) -> None:
        if self.bitSet[idx]==str(1):
            self.number_of_zero+=1
            self.number_of_ones-=1
        self.bitSet[idx]=str(0)
        self.image[idx]=str(1)
    def flip(self) -> None:
        self.bitSet,self.image=self.image,self.bitSet
        self.number_of_ones,self.number_of_zero=self.number_of_zero,self.number_of_ones
    def all(self) -> bool:
        return self.number_of_zero==0
    def one(self) -> bool:
        return self.number_of_ones>=1
    def count(self) -> int:
        return self.number_of_ones
    def toString(self) -> str:
        return "".join(self.bitSet)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()