class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left=0
        right=len(nums)-1
        counter=0
        while left<right:
            current=nums[left]+nums[right]
            if current==k:
                counter+=1
                left=left+1
                right=right-1
            elif current>k:
                right=right-1
            else:
                left=left+1
        return counter

        