class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        length=len(nums)
        result=0
        for i in range(length):
            for j in range(i,length):
                temp=set(list(nums[i:j+1]))
                result+=len(temp)**2

        return result
        