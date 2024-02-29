class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left=0
        right=1
        maxsum=0
        length=len(nums)
        while right<length:
            maxsum+=nums[left]
            left=left+2
            right=right+2
        return maxsum

        