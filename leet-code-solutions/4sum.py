class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                left=j+1
                right=len(nums)-1
                while left<right:
                    current=nums[i]+nums[j]+nums[left]+nums[right]
                    if current==target:
                        result.add((nums[i],nums[j],nums[left],nums[right]))
                        left=left+1
                        right=right-1
                    elif current>target:
                        right=right-1
                    else:
                        left=left+1
        return [list(value) for value in result]
        