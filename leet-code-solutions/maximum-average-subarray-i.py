class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left,right=0,k
        maxSum,current=sum(nums[0:k]),sum(nums[0:k])
        while right<len(nums):
            current+=nums[right]-nums[left]
            maxSum=max(maxSum,current)
            left=left+1
            right=right+1
        return maxSum/k
