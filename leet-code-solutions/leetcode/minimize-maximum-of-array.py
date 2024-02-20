class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        currentMax=nums[0] 
        currentSum=currentMax
        for i in range(1,len(nums)):
            currentSum+=nums[i]
            currentMax=max(currentMax,currentSum/(i+1))
        return ceil(currentMax)
