class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        largest=0
        for i in range(len(nums)-2):
            if nums[i]+nums[i+1]>nums[i+2]:
                preVal=nums[i]+nums[i+1]+nums[i+2]
                largest=max(largest,preVal)
        return largest

        