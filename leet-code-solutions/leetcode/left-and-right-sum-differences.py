class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum=[0]*(len(nums)+1)
        for i in  range(1,len(nums)+1):
            leftSum[i]=leftSum[i-1]+nums[i-1]
        result=[0]*len(nums)
        total=sum(nums)
        for i in range(len(nums)):
            result[i]=abs(leftSum[i]-(total-leftSum[i+1]))
        return result
        