class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left,right=0,len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                return [bisect_left(nums,nums[mid]),bisect_right(nums,nums[mid])-1]
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return [-1,-1]
        