class Solution:
    def findMin(self, nums: List[int]) -> int:
        length=len(nums)

        if nums[0]<=nums[-1]:
            return nums[0]
        left,right=0,length-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]<nums[mid-1]:
                return nums[mid]
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            if nums[mid]>nums[0]:
                left=mid+1
            else:
                right=mid-1




        