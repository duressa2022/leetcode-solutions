class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left=[0]*(len(nums)+1)
        right=[0]*(len(nums)+1)
        for i in range(1,len(nums)+1):
            left[i]=left[i-1]+nums[i-1]
        nums=nums[::-1]
        for i in range(1,len(nums)+1):
            right[i]=right[i-1]+nums[i-1]
        right=right[::-1]
        for i in range(len(left)-1):
            if left[i]==right[i+1]:
                return i
        return -1

        