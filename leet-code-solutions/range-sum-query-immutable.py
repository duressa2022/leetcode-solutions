class NumArray:

    def __init__(self, nums: List[int]):
        self.numbers=nums

    def sumRange(self, left: int, right: int) -> int:
        prefixSum=[0]*(len(self.numbers)+1)
        for i in range(1,len(self.numbers)+1):
            prefixSum[i]=prefixSum[i-1]+self.numbers[i-1]
        return prefixSum[right+1]-prefixSum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)