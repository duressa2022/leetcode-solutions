class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result=0
        left,right=0,1
        length=len(nums)
        while right<length:
            if nums[left]>=nums[right]:
                current=abs(nums[left]-nums[right])+1
                nums[right]+=current
                result+=current
            left=left+1
            right=right+1
        return result


        