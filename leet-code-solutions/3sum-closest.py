class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest=float("inf")
        nums.sort()
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while left<right:
                current=nums[i]+nums[left]+nums[right]
                if abs(closest-target) >abs(current-target):
                    closest=current
                elif current>target:
                    right=right-1
                else:
                    left=left+1
        return closest

        