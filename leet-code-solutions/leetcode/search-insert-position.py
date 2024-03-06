class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        result=0
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
                result=mid
            else:
                left=mid+1
                result=mid+1
        return result
        