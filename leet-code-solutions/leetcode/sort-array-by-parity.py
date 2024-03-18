class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left=-1
        length=len(nums)
        for right in range(length):
            if nums[right]%2==0:
                left=left+1
                (nums[left],nums[right])=(nums[right],nums[left])
        return nums
    
        