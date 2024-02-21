class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        length=len(nums)
        counter=0
        for i in range(length-2):
            left,right=i+1,length-1
            while left<right:
                current=nums[left]+nums[right]
                if nums[i]<current:
                    counter+=right-left
                    left=left+1
                else:
                    right=right-1
        return counter


        