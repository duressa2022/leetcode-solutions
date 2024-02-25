class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        length=len(nums)
        currentVal=len(set(nums))
        result=left=0
        for right in range(length):
            while currentVal==len(set(nums[left:right+1])):
                result+=length-(right+1)+1
                left=left+1
        return result



        