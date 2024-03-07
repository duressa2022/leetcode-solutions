class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        left,right,counter=0,len(nums)-1,0
        nums.sort()
        while left<=right:
            if nums[left]+nums[right]<=target:
                counter+=pow(2,right-left)
                left=left+1
            else:
                right=right-1
        return counter%(10**9+7)
        