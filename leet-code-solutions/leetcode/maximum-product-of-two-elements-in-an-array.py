class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        first=nums[len(nums)-1]
        second=nums[len(nums)-2]
        return (first-1)*(second-1)
        