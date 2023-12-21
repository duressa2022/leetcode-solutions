class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length=-float("inf")
        slow=0
        fast=0
        counter=0
        while fast<len(nums):
            if nums[slow]==nums[fast] and nums[fast]==1:
                counter+=1
                fast+=1
            else:
                if nums[fast]==0:
                    fast=fast+1
                max_length=max(max_length,counter)
                slow=fast
                counter=0
        return max(max_length,counter)


    


        