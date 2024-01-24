class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum=0
        for i in range(len(nums)):
            runningSum+=nums[i]
            nums[i]=runningSum
        return nums
